import React from 'react';
import Button from '@mui/material/Button';

import './MyServices.scss'
import Popup from '../../popup/ApplicationPopup'


const ServiceItem = ({title, text}) => {
    const [open, setOpen] = React.useState(false);

    const handleClickOpen = () => {
      setOpen(true);
    };
  
    const handleClose = () => {
      setOpen(false);
    };

    return (
        <div className="item">
            <h4 className="item_title">{title}</h4>
            <p className="item_text">{text}</p>
            <p className="item_price">Цена: <b>договорная</b></p>
            <Button className='item_order' variant="outlined" onClick={handleClickOpen}>
                Заказать
            </Button>
            <Popup openPopup={open} handleClose={handleClose} />
        </div>
    )
}


export default function MyServices() {
    const site_service_title = 'Создание сайта'
    const site_service_text = 'Создаем качественные и масштабируемые веб-приложения на базе Django, Flask или FastAPI с использованием современных баз данных. Мы уделяем особое внимание архитектуре, соблюдая принципы чистого кода и SOLID. Наш подход гарантирует высокую производительность, безопасность и удобство эксплуатации вашего проекта.'
    
    const bot_service_title = 'Разработка чат-ботов'
    const bot_service_text = 'Создаем эффективных и надежных чат-ботов на базе Python, интегрированных с Telegram, WhatsApp и другими платформами. Мы разрабатываем ботов с чистой архитектурой и продуманной логикой, обеспечивая стабильную работу, удобное взаимодействие с пользователями и легкость в последующем расширении функционала.'
    
    return(
        <div className="main__my_services" id="my_services" style={{ scrollMarginTop: "10rem" }}>
            <h2>Услуги</h2>
            <div className="service_items">
                <ServiceItem title={site_service_title} text={site_service_text} />
                <ServiceItem title={bot_service_title} text={bot_service_text} />
            </div>
        </div>
    )
}
