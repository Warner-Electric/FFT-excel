
# Excel FFT Processor

## Description
This program reads an Excel file containing time series data and signal data, performs Fast Fourier Transform (FFT) on the signal data, and generates various plots to visualize the frequency components of the signal. The program includes the following plots:
- Amplitude Spectrum
- Power Spectral Density (PSD)
- Phase Spectrum
- Logarithmic Scale Amplitude Spectrum
- Spectrogram
- Waterfall Plot (3D FFT Result)

## Equations Used
### Fast Fourier Transform (FFT)
The FFT is used to compute the discrete Fourier transform (DFT) of a sequence. The DFT is defined as:

$$\[ X(k) = \sum_{n=0}^{N-1} x(n) \cdot e^{-j \cdot 2\pi \cdot k \cdot n / N} \]$$
where:
- $$\( X(k) \) is the DFT result at frequency bin \( k \)$$
- $$\( x(n) \) is the input signal at time index \( n \)$$
- $$\( N \) is the number of samples in the input signal$$
- $$\( j \) is the imaginary unit$$

### Power Spectral Density (PSD)
The PSD is computed as the square of the magnitude of the FFT result:
$$\[ P(k) = |X(k)|^2 \]$$
where:
- $$\( P(k) \) is the power at frequency bin \( k \)$$
- $$\( X(k) \) is the FFT result at frequency bin \( k \)$$

### Phase Spectrum
The phase spectrum is computed as the angle of the FFT result:
$$\[ \phi(k) = 	ext{angle}(X(k)) \]$$
where:
- $$\( \phi(k) \) is the phase at frequency bin \( k \)$$
- $$\( X(k) \) is the FFT result at frequency bin \( k \)$$

## Usage
1. Run the program.
2. Click on the "Select Excel File" button to open a file dialog and select an Excel file containing time series data and signal data.
3. The program will read the data, perform FFT, and generate various plots to visualize the frequency components of the signal.

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- tkinter
- openpyxl

![image](https://github.com/user-attachments/assets/751488bd-03a3-4b80-9ffe-271c13838f95)


