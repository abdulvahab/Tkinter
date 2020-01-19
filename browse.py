import tkinter as tk
from tkinter import filedialog as fd, StringVar

'''This is a module to convert csv files in a 'input_dir/base_dir' 
to shp files and write n into 'output_dir/base_dir'
'''
import geopandas as gpd
import pandas as pd
import os
import re
from geopandas import GeoDataFrame, points_from_xy

import argparse
parser = argparse.ArgumentParser()
#-i specify path for csv files's folder -o specify path for shp files's folder 
parser.add_argument("-i", "--input", dest = "input_csv_folder", default = "", help="path for csv files's folder")
parser.add_argument("-o", "--output", dest = "output_shp_folder", default = "", help="path for shp files's folder")


args = parser.parse_args()

print( "CSV folder {} shp folder  {}".format(
        args.input_csv_folder,
        args.output_shp_folder,
        ))

def csv_to_shp(csv_file_path, shp_file_path):

    df = pd.read_csv(csv_file_path, sep=' ', header=None)
    df.columns = ['lat', 'lon', 'precp']
    #df['geometry'] = df.apply(lambda row: Point(row.lon, row.lat), axis=1)
    gdf = GeoDataFrame(df, geometry=points_from_xy(df.lon, df.lat))
    gdf = GeoDataFrame(df, crs={'init':'epsg:4326'})
    gdf = gdf.to_crs({'init': 'epsg:2326'})
    gdf['geometry'] = gdf.buffer(265).envelope
    gdf.to_file(shp_file_path)

def run(input_dir = 'swirls_csv_files',output_dir = 'swirls_shp_files'):
 
    for base_dir in os.listdir(input_dir): 
        if base_dir.startswith('.'):
            continue 
        else:
            base_dir_csv = f"{input_dir}/{base_dir}"
            base_dir_shp = f"{output_dir}/{base_dir}"
            if base_dir not in os.listdir(output_dir): 
                os.mkdir(base_dir_shp)
            csv_files = os.listdir(base_dir_csv)
    
        for csv_file in csv_files:
            csv_file_path = f"{base_dir_csv}/{csv_file}"
            shp_file = re.search(r'.*\_.*\_.*\_(.*\_.*)\..+',csv_file).groups()[0] + '.shp'
            shp_file_path = f"{base_dir_shp}/{shp_file}"
            csv_to_shp(csv_file_path, shp_file_path)


class Browse(tk.Frame):
    """ Creates a frame that contains a button when clicked lets the user to select
    a file and put its filepath into an entry.
    """

    def __init__(self, master, initialdir='', filetypes=()):
        super().__init__(master)
        self.filepath = tk.StringVar()
        self._initaldir = initialdir
        self._filetypes = filetypes
        self._create_widgets()
        self._display_widgets()
        self.input_dir = tk.StringVar()
        self.output_dir = tk.StringVar()

    def _create_widgets(self):
        self._entry = tk.Entry(self, textvariable=self.filepath)
        self._button = tk.Button(self, text="Browse...", command=self.browse)
        self._input_folder= tk.Button(self, text="Choose input folder", bg="red",command= self.select_input_folder)
        self._output_folder = tk.Button(self, text="Choose output folder", bg="green",command= self.select_output_folder)
        self.convert = tk.Button(self, text="Convert .csv to .shp", bg="green", command = self.convert_csv_2_shp)

    def _display_widgets(self):
        self._entry.pack(fill='x', expand=True)
        self._button.pack(anchor='se')
        self._input_folder.pack()
        self._output_folder.pack()
        self.convert.pack()

    def browse(self):
        """ Browses a .png file or all files and then puts it on the entry.
        """

        self.filepath.set(fd.askopenfilename(initialdir=self._initaldir,
                                             filetypes=self._filetypes))
    def select_input_folder(self):
        self.input_dir.set(fd.askdirectory())

    def select_output_folder(self):
        self.output_dir.set(fd.askdirectory())
    def convert_csv_2_shp(self):
        print(self.input_dir)
        print(self.output_dir)
        run(self.input_dir.get(), self.output_dir.get())
    


if __name__ == '__main__':
    root = tk.Tk()
    root.title(".csv to .shp file conversion Application")
    file_browser = Browse(root, initialdir=r"C:\Users",
                                filetypes=(('Portable Network Graphics','*.png'),
                                                            ("All files", "*.*")), )
    file_browser.pack(fill='x', expand=True)

    #root.withdraw()
    
    #selected_folder = select_folder()

    '''
    input_folder = tk.Button(root, text="Choose input folder", bg="red",command= button)
    input_folder.pack()
    input_dir = selected_folder.get()

    #selected_folder = select_folder()
    output_folder = tk.Button(root, text="Choose output folder", bg="green",command= button)
    output_folder.pack()
    output_dir = selected_folder.get()

    convert = tk.Button(root, text="Convert .csv to .shp", bg="green", command = lambda : run(input_dir, output_dir))
    convert.pack()
    ''' 
 
    root.mainloop()