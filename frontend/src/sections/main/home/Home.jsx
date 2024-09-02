import React, { useEffect, useRef } from 'react';
import Typed from 'typed.js';

import { FaTelegramPlane, FaWhatsapp, FaGithub } from "react-icons/fa";
import { SiGmail } from "react-icons/si";

import './Home.scss'


const TypedComponent = () => {
    const typedRef = useRef(null);
    const el = useRef(null);
  
    useEffect(() => {
      const options = {
        strings: ['Создаю надежные <br /> <b> сайты </b>  и  чат <b> боты</b>.'],
        typeSpeed: 35,
      };
  
      typedRef.current = new Typed(el.current, options);
  
      return () => {
        typedRef.current.destroy();
      };
    }, []);
  
    return (
      <div>
        <span ref={el} />
      </div>
    );
};


const Contacts = () => {
    return (
        <ul className='main__home_contacts'>
            <a href="https://t.me/anciv_dpl"><li><FaTelegramPlane color='131313' size={20}/></li></a>
            <a href=""><li><FaWhatsapp color='131313' size={20} /></li></a>
            <a href="https://github.com/anciv96"><li><FaGithub color='131313' size={20} /></li></a>
            <a href="mailto:anciv96@gmail.com"><li><SiGmail color='131313' size={20} /></li></a>
        </ul>
    )
}


export default function Home() {
    return(
        <div className="main__home" id="contacts" style={{ scrollMarginTop: "10rem" }}>
            <div className='main_text'>
                <TypedComponent/>
            </div>
            <Contacts/>
        </div>
    )
} 