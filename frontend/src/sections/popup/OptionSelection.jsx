import React from 'react';

import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';

import './OptionSelection.scss';


// export default function OptionSelection({ options, name, value, onChange }) {
//     const handleAlignment = (event, newAlignment) => {
//         onChange({ target: { name, value: newAlignment } });
//       };
    
//     return (
//         <ToggleButtonGroup
//             value={value} // Устанавливаем текущее значение из props
//             exclusive
//             onChange={handleAlignment} // Вызываем handleAlignment при изменении выбора
//             className='choices'
//         >
//             {
//                 options.map((option, i) => (
//                     <ToggleButton value={option} aria-label={option} key={i} className='choice'>
//                         {option}
//                     </ToggleButton>
//                 ))
//             }
//         </ToggleButtonGroup>
//     )
// }
export default function OptionSelection({ options, name, value, onChange, required }) {
    const handleAlignment = (event, newAlignment) => {
        onChange({ target: { name, value: newAlignment } });
    };

    return (
        <div className={`option-selection ${required && !value ? 'required' : ''}`}>
            <ToggleButtonGroup
                value={value}
                exclusive
                onChange={handleAlignment}
                className='choices'
                aria-labelledby={`${name}-label`}
            >
                {options.map((option, i) => (
                    <ToggleButton value={option} aria-label={option} key={i} className='choice'>
                        {option}
                    </ToggleButton>
                ))}
            </ToggleButtonGroup>
            {required && !value && <p className="error-message">Это поле обязательно</p>}
        </div>
    );
}