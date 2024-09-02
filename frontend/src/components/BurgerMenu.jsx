import * as React from 'react';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import Button from '@mui/material/Button';
import { IoClose } from "react-icons/io5";
import { CiMenuFries } from "react-icons/ci";

import Menu from '../components/Menu'
import HeaderConnectBtn from './HeaderConnectButton';

import './BurgerMenu.scss'


export default function BurgerMenu() {
    const [openBurgerMenu, setOpenBurgerMenu] = React.useState(false);

    const toggleDrawer = (openBurgerMenu) => (event) => {
      if (event.type === 'keydown' && (event.key === 'Tab' || event.key === 'Shift')) {
        return;
      }
      setOpenBurgerMenu(openBurgerMenu);
      
    };
      

    return (
        <div className='burger_menu'>
            <Button onClick={toggleDrawer(true)} >
                <CiMenuFries color='#fff' size={25} />
            </Button>
            <Drawer
                anchor="top"
                open={openBurgerMenu}
                onClose={toggleDrawer(false)}
            >
                <BurgerMenuContent 
                    toggleDrawer={toggleDrawer}
                />
            </Drawer>
        </div>
    );
}



const BurgerMenuContent = ({toggleDrawer}) => {
    return(
        <Box
            sx={{ width: 'auto' }}
            role="presentation"
            className="burger_menu_content"
        >
            <IoClose 
                onClick={toggleDrawer(false)} 
                className='close_btn'
                size={20}
                color='#b4b4b4'
            />
            
            <Box onClick={toggleDrawer(false)}>
                <Menu/>
            </Box>
            
            <HeaderConnectBtn/>
        </Box>
    )
}
