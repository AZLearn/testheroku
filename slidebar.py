
import streamlit as st

def main():

	x = st.slider('x')  # ?? this is a widget
	st.write(x, 'squared is', x * x)
	
if __name__ == '__main__':
	main()