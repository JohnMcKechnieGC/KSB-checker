from tkinter import Tk, filedialog

# Use TkInter to open a file dialog
# Hide the root Tkinter window
root = Tk()
root.withdraw()

# Bring the root window to the front (even though it's hidden)
root.attributes('-topmost', True)
root.lift()
root.focus_force()


def files_to_open(extension):
    """
    Wrapper for the open multiple files dialog
    """
    filenames = filedialog.askopenfilenames(
        title=f"Select {extension.upper()} files",
        filetypes=[(f"{extension.upper()} files", f"*.{extension}")]
    )
    if isinstance(filenames, str):
        return filenames,
    return filenames


def file_to_open(extension: str) -> str:
    """
    Wrapper for the open single file dialog
    """
    filename = filedialog.askopenfilename(
        title=f"Select {extension.upper()} files",
        filetypes=[(f"{extension.upper()} files", f"*.{extension}")]
    )
    return filename


def file_to_save(extension: str) -> str:
    """
    Wrapper for the save file dialog
    """
    filename = filedialog.asksaveasfile(
        title=f"Select {extension.upper()} files",
        filetypes=[(f"{extension.upper()} files", f"*.{extension}")]
    )
    return filename