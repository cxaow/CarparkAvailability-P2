class CarparkFinderError(Exception):
    # Base exception for application.
    pass

class HistorySaveError(CarparkFinderError):
    # Failed to save history; existing data preserved.
    pass

class FavouriteSaveError(CarparkFinderError):
    # Failed to save favourite.
    pass

class APICarparkError(CarparkFinderError):
    # API/data retrieval failed.
    pass