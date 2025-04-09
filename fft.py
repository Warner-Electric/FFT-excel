import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Function to read an Excel file, perform FFT, and graph the results
def process_excel_fft(file_path, time_base=None):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path, engine='openpyxl')
        
        # Extract time and signal data
        time = df['Time'].values
        signal = df['Signal'].values
        
        # If a custom time base is provided, adjust the time array
        if time_base is not None:
            time = np.arange(0, len(signal) * time_base, time_base)
        
        # Perform FFT
        fft_result = np.fft.fft(signal)
        
        # Get the frequencies corresponding to the FFT result
        freqs = np.fft.fftfreq(len(fft_result), d=(time[1] - time[0]))
        
        # Create subplots for different visualizations
        fig, axs = plt.subplots(3, 2, figsize=(12, 12))
        
        # Plot the FFT result (Amplitude Spectrum)
        axs[0, 0].plot(freqs, np.abs(fft_result))
        axs[0, 0].set_xlabel('Frequency')
        axs[0, 0].set_ylabel('Amplitude')
        axs[0, 0].set_title('Amplitude Spectrum')
        
        # Plot the Power Spectral Density (PSD)
        psd = np.abs(fft_result)**2
        axs[0, 1].plot(freqs, psd)
        axs[0, 1].set_xlabel('Frequency')
        axs[0, 1].set_ylabel('Power')
        axs[0, 1].set_title('Power Spectral Density (PSD)')
        
        # Plot the Phase Spectrum
        phase = np.angle(fft_result)
        axs[1, 0].plot(freqs, phase)
        axs[1, 0].set_xlabel('Frequency')
        axs[1, 0].set_ylabel('Phase')
        axs[1, 0].set_title('Phase Spectrum')
        
        # Plot the FFT result on a logarithmic scale
        axs[1, 1].plot(freqs, np.log(np.abs(fft_result)))
        axs[1, 1].set_xlabel('Frequency')
        axs[1, 1].set_ylabel('Log Amplitude')
        axs[1, 1].set_title('Logarithmic Scale Amplitude Spectrum')
        
        # Plot the Spectrogram
        axs[2, 0].specgram(signal, Fs=1/(time[1] - time[0]))
        axs[2, 0].set_xlabel('Time')
        axs[2, 0].set_ylabel('Frequency')
        axs[2, 0].set_title('Spectrogram')
        
        # Plot the Waterfall Plot (3D plot)
        ax3d = fig.add_subplot(3, 2, 6, projection='3d')
        ax3d.plot(freqs, np.abs(fft_result), zs=0, zdir='z', label='Amplitude Spectrum')
        ax3d.set_xlabel('Frequency')
        ax3d.set_ylabel('Amplitude')
        ax3d.set_zlabel('Z')
        ax3d.set_title('Waterfall Plot (3D FFT Result)')
        
        # Adjust layout
        plt.tight_layout()
        
        # Show the plot window
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to open a file dialog and select an Excel file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        try:
            time_base = float(time_base_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid time base value. Please enter a valid number.")
            return
        process_excel_fft(file_path, time_base=time_base)

# Create the main window
root = tk.Tk()
root.title("Excel FFT Processor")

# Create and place a button to select a file
select_button = tk.Button(root, text="Select Excel File", command=select_file)
select_button.pack(pady=20)

# Create an entry widget for the time base
time_base_label = tk.Label(root, text="Enter Time Base (seconds):")
time_base_label.pack(pady=5)
time_base_entry = tk.Entry(root)
time_base_entry.pack(pady=5)

# Create a text widget to display instructions for Excel formatting
instructions_text = tk.Text(root, wrap=tk.WORD)
instructions_text.insert(tk.END, "Instructions for Excel Formatting:\n\n")
instructions_text.insert(tk.END, "1. Ensure your Excel file has two columns: 'Time' and 'Signal'.\n")
instructions_text.insert(tk.END, "2. The 'Time' column should contain time values in seconds.\n")
instructions_text.insert(tk.END, "3. The 'Signal' column should contain corresponding signal values.\n")
instructions_text.insert(tk.END, "4. Save your Excel file with a .xlsx extension.\n")
instructions_text.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
