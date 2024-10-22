from menus import get_info, show_menu, welcome

def run_app() :
    welcome()
    patient_info = get_info ()
    show_menu(patient_info)