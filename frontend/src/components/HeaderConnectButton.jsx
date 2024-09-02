import * as React from 'react';
import Button from '@mui/material/Button';

import Popup from '../sections/popup/ApplicationPopup'

import './HeaderConnectButton.scss'


const HeaderConnectBtn = () => {
    const [openPopup, setOpenPopup] = React.useState(false);

    const handleClickOpenPopup = () => {
        setOpenPopup(true);
    };
  
    const handleClosePopup = () => {
        setOpenPopup(false);
    };

    return (
        <div className="header__connect_btn">
            <Button variant="outlined" onClick={handleClickOpenPopup} sx={{
                all: 'unset',
                backgroundColor: 'transparent',
                padding: 0,
                margin: 0,
                border: 'none',
                color: 'inherit',
                fontFamily: 'inherit',
                fontSize: 'inherit',
                textTransform: 'none',
                '&:hover': {
                    border: "none",
                    backgroundColor: 'transparent',

                },
            }}>
                Связаться
            </Button>
            <Popup openPopup={openPopup} handleClose={handleClosePopup} />
        </div>
    )
}

export default HeaderConnectBtn
