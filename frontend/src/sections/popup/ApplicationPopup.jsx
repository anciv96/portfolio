import * as React from 'react';
import Dialog from '@mui/material/Dialog';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import Slide from '@mui/material/Slide';

import './ApplicationPopup.scss'
import PopupContent from './PopupContent'


const Transition = React.forwardRef(function Transition(props, ref) {
  return <Slide direction="up" ref={ref} {...props} />;
});


export default function Popup({openPopup, handleClose}){
    return(
        <React.Fragment>
            <Dialog
                open={openPopup}
                TransitionComponent={Transition}
                keepMounted
                onClose={handleClose}
                aria-describedby="alert-dialog-slide-description"
                className='popup'
            >
                <DialogContent sx={{padding: "0"}}>
                    <DialogContentText id="alert-dialog-slide-description" >
                        <PopupContent/>
                    </DialogContentText>
                </DialogContent>
            </Dialog>
        </React.Fragment>
    )
}
