import { useEffect, useState } from 'react'
import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay } from 'swiper/modules';
import axios from 'axios';


import 'swiper/css';

import './Feedbacks.scss'
import { API_ENDPOINTS } from '../../../apiConfig'
import ClampedText from '../../../components/ClampText';


const Item = ({author, feedback}) => {

    return(
        <div className="feedback_item">
            <p className="feedback_author">{author}</p>
            <ClampedText text={feedback} lines={10} />
        </div>
    )
}


export default function Feedbacks() {
    const [feedbacks, setFeedbacks] = useState([])
    useEffect(() => {
        axios.get(API_ENDPOINTS.feedbacks)
        .then(response => {
            setFeedbacks(response.data)
            console.log(response.data)
        })
        .catch(error => {
            console.log('Error fetching texts:', error)
        })
    }, [])
    return(
        <div className="main__feedbacks" id='feedbacks' style={{ scrollMarginTop: "10rem" }}>
            <h2>Отзывы</h2>
            <div className="feedback_items">
                <Swiper 
                    className="mySwiper"
                    slidesPerView="auto"
                    spaceBetween={25}
                    loop={true}
                    autoplay={{
                        delay: 3000,
                    }}
                    modules={[Autoplay]}
                    
                >
                    {
                        feedbacks.map((feedback, id) => (
                            <SwiperSlide key={id}>
                                <a href={feedback.url}>
                                    <Item author={feedback.author} feedback={feedback.text} />
                                </a>
                            </SwiperSlide>
                        ))
                    }

                </Swiper>
            </div>
        </div>
    )
}