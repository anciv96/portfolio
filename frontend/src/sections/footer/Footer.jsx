import Logo from '../../components/Logo'
import Menu from '../../components/Menu'
import './Footer.scss'

export default function Footer () {
    return(
        <footer>
            <Logo/>
            <Menu vertical={true}/>
        </footer>
    )
}
