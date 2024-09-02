import React from 'react';


import './Header.scss'
import Logo from '../../components/Logo'
import Menu from '../../components/Menu'
import BurgerMenu from '../../components/BurgerMenu';
import HeaderConnectBtn from '../../components/HeaderConnectButton';



export default function Header(){
    return (
        <header>
            <Logo/>
            <Menu />
            <BurgerMenu/>
            <HeaderConnectBtn/>
        </header>
    )
}
