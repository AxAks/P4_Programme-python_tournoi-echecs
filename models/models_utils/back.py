# coding=utf-8

def back(self) -> None:
    """
    This method enables to go back to the previous screen
    if the screen is the root menu, it directs to the controller to make the program quit.
    """
    if self.root_page:
        self.quit()
    else:
        self.previous_page.run()
