# global_controller_functions.py

def raise_page(self, page_name: str) -> None:
        """ Takes the page name as an argument and shows the page in the window while hiding all others.

        Args:
            page_name (str): Name of the page from the all_pages dictionary keys.
        """
        page_object = self.all_pages[page_name]
        page_object.tkraise()