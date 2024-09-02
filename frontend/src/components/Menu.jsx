import './Menu.scss'


export default function Menu() {
    return (
            <div className="menu">
                <ul>
                    <li><a href="#contacts">Контакты</a></li>
                    <li><a href="#about_me">О себе</a></li>
                    <li><a href="#my_services">Услуги</a></li>
                    <li><a href="#portfolio">Портфолио</a></li>
                    <li><a href="#feedbacks">Отзывы</a></li>
                </ul>
            </div>
    )
}