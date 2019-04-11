"""
Sudoku solution tactics.  These include the
constraint propogation tactics and (in phase
two) the search-based solver.

Author: FIXME
"""

from sdk_board import Board
import sdk_tile

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def naked_single(board: Board) -> bool:
    """As described in http://www.sadmansoftware.com/sudoku/nakedsingle.php
    Returns True iff some change has been made
    """
    logging.info("Applying naked single tactic")
    changed = False
    for group in board.groups:
        changed = group.naked_single_constrain() or changed
    return changed


def hidden_single(board: Board) -> bool:
    """As described in http://www.sadmansoftware.com/sudoku/hiddensingle.php
    Returns True iff some change has been made
    """
    logging.info("Applying hidden single tactic")
    changed = False
    for group in board.groups:
        changed = group.hidden_single_constrain() or changed
    return changed


def propagate(board: Board):
    """Propagate constraints until we either solve the puzzle,
    show the puzzle as given is unsolvable, or can make no more
    progress by constraint propagation.
    """
    logging.info("Propagating constraints")
    changed = True
    while changed:
        logging.info("Invoking naked single")
        changed = naked_single(board)
        if board.is_solved() or not board.is_consistent():
            return
        changed = hidden_single(board) or changed
        if board.is_solved() or not board.is_consistent():
            return
    return


def solve(board: Board) -> bool:
    """Main solver.  Initially this just invokes constraint
    propagation.  In phase 2 of the project, you will add
    recursive back-tracking search (guess-and-check with recursion).
    """
    log.debug("Called solve on board:\n{}".format(board))
    propagate(board)

    if board.is_solved():
        return True
    elif not board.is_consistent():
        return False

    # min number of candidates a tile is allowed to have
    # In this case I chose 9 because if it has ANY candidates
    # and no value, it needs to be changed
    min_candidates = 9

    # Check every tile in the board
    for group in board.groups:
        for tile in group.tiles:

            # if the tile is empty and has ANY candidates, choose set tile for changing
            if tile.value == "." and len(tile.candidates) <= min_candidates:
                change_tile = tile


    # save the board at an unaltered state
    saved_board = board.as_list()

    # Try out each candidate in the tile we chose for changing
    for candidate in change_tile.candidates:
        change_tile.set_value(candidate)

        # Recursive step: if this does the trick, we did it
        if solve(board):
            return True

        # If not...  >:(  reset board and try again
        else:
            board.set_tiles(saved_board)

    return False
