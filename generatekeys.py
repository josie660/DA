import streamlit
import pickle 
from pathlib import Path
import streamlit_authenticator as stauth

names=['marie jose marroun', 'mabelle marroun', 'reina marroun', 'rita akkary', 'perla']
usernames=['mariejose', 'mabelle','reina', 'rita','perla']
passwords=['abc123', 'qwerty', 'asdfg', 'dsfjfk','lalala']
hashed_passwords = stauth.Hasher(passwords).generate()

file_path=Path(__file__).parent/'hashed_pw.pkl'
with file_path.open('wb') as file:
    pickle.dump(hashed_passwords, file)
