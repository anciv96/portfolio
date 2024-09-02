
import Home from './home/Home'
import AboutMe from './about_me/AboutMe'
import MyServices from './my_services/MyServices'
import Portfolio from './portfolio/Portfolio'
import Feedbacks from './feedbacks/Feedbacks'
import './Main.scss'


export default function Main(){

    return(
        <main>
            <Home/>
            <AboutMe/>
            <MyServices/>
            <Portfolio/>
            <Feedbacks/>
        </main>
    )
}