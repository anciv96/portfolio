import Divider from '@mui/material/Divider';

import './App.css';

import Header from './sections/header/Header'
import Main from './sections/main/Main'
import Footer from './sections/footer/Footer'

import Popup from './sections/popup/ApplicationPopup'

function App() {
  return (
    <>
      <Header />
      <Main/>

      <Popup/>

      <Divider sx={{background: "#fff"}} />

      <Footer/>
    </>
  );
}

export default App;
