import Tooltip, { tooltipClasses } from '@mui/material/Tooltip';
import { styled } from '@mui/material/styles';


import logo from '../img/logo.jpg'
import './AboutMe.scss'


const BootstrapTooltip = styled(({ className, ...props }) => (
    <Tooltip {...props} arrow classes={{ popper: className }} />
    ))(({ theme }) => ({
    [`& .${tooltipClasses.arrow}`]: {
      color: theme.palette.common.black,
    },
    [`& .${tooltipClasses.tooltip}`]: {
      backgroundColor: '#fff',
      color: 'black',
      fontSize: '.75rem',
      padding: '1rem',
      letterSpacing: '0.04rem',
      lineHeight: "120%",
    },
}));


export default function AboutMe() {

    const frontend_meaning =  "Frontend-разработчик — это специалист, который занимается разработкой пользовательского интерфейса, то есть той части сайта или приложения, которую видят посетители страницы."
    const backend_meaning =  "Back-end (бэкенд) разработка - это создание серверной части в веб-приложениях. То есть backend разработчики имеют дело со всем, что относится к базам данных, архитектуре, программной логике — в общем, со всем, что обычный пользователь не видит."

    return (
        <div className="main__about_me" id="about_me" style={{ scrollMarginTop: "10rem" }}>
            <div className="about_me_info">
                <h4 className=""> <b>{'>>>'}</b> Привет! Я Ансаф.</h4>
                <div className='about_me_text'>
                    <div className='about_me_text_item'>
                        Я веб-разработчик, создаю сайты и чат боты под ключ. Как правило “творю” один, но в особых случаях работаю в связке с <span><BootstrapTooltip title={frontend_meaning}>фронтендером</BootstrapTooltip></span>. 
                    </div>
                    <div className='about_me_text_item'>
                        Моя специализация <span><BootstrapTooltip title={backend_meaning}>backend разработка</BootstrapTooltip></span>. Занимаюсь серверной архитектурой, управлением базами данных и реализацией бизнес-логики. Но также имею опыт работы с frontend’ом и могу разработать внешний интерфейс вашего проекта
                    </div>
                    <div className='about_me_text_item'>
                        Частый стек разработки – Django, FastAPI, Flask, React, Aiogram, MySQL, PosrgreSQL ... .
                    </div>
                </div>
            </div>
            <div className="about_me_photo" >
                <img src={logo} alt="logo" />
            </div>
        </div>
    )
}

