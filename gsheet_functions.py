import gspread


def clear_import_tab(credentials, sheet_id):
    """Clear the current data in the import tab."""
    gc = gspread.service_account(filename=credentials)
    sheet = gc.open_by_key(sheet_id)
    import_tab = sheet.worksheet('import')
    aux_tab = sheet.worksheet('aux')

    last_used_row = aux_tab.acell('B1').value

    clearing_range = []

    for row in range(2, int(last_used_row) + 1):
        clearing_range.append(['', '', '', '', '', '', '', '', ''])

    import_tab.update('A{}:I{}'.format(2, last_used_row), clearing_range)

    print('import tab cleared successfully')


def import_data(credentials, sheet_id, data):
    """Import the provided data into the import tab on the provided sheet."""
    gc = gspread.service_account(filename=credentials)
    sheet = gc.open_by_key(sheet_id)
    import_tab = sheet.worksheet('import')

    import_tab.update('A{}:I{}'.format(2, len(data) + 1), data)

    print('data imported successfully')
