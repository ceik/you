import sys

import mongo_functions
import gsheet_functions

import config


def main(data_file):
    """"""
    mongo_functions.drop_order_items()
    mongo_functions.import_order_items(data_file)

    data = mongo_functions.get_order_items()

    gsheet_functions.clear_import_tab(config.GSHEET_CREDENTIALS,
                                      config.GSHEET_SHEET_ID)
    gsheet_functions.import_data(config.GSHEET_CREDENTIALS,
                                 config.GSHEET_SHEET_ID, data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('Missing argument: Path to data file')
    main(sys.argv[1])
