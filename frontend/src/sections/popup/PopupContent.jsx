// import TextField from '@mui/material/TextField';
// import { createTheme, ThemeProvider, useTheme } from '@mui/material/styles';
// import { outlinedInputClasses } from '@mui/material/OutlinedInput';

// import { useCallback, useState } from 'react';
// import axios from 'axios';
// import { API_ENDPOINTS } from '../../apiConfig';
// import OptionSelection from './OptionSelection';
// import './PopupContent.scss';


// const MAX_FILE_SIZE_MB = 5 * 1024 * 1024; // 5 MB


// const createCustomTheme = (outerTheme) => createTheme({
//   palette: {
//     mode: outerTheme.palette.mode,
//   },
//   components: {
//     MuiTextField: {
//       styleOverrides: {
//         root: {
//           '--TextField-brandBorderColor': '#E0E3E7',
//           '--TextField-brandBorderHoverColor': '#B2BAC2',
//           '--TextField-brandBorderFocusedColor': '#6F7E8C',
//           '& label.Mui-focused': {
//             color: 'var(--TextField-brandBorderFocusedColor)',
//           },
//         },
//       },
//     },
//     MuiOutlinedInput: {
//       styleOverrides: {
//         root: {
//           color: '#fff',
//           [`&:hover .${outlinedInputClasses.notchedOutline}`]: {
//             borderColor: 'var(--TextField-brandBorderHoverColor)',
//           },
//           [`&.Mui-focused .${outlinedInputClasses.notchedOutline}`]: {
//             borderColor: 'var(--TextField-brandBorderFocusedColor)',
//           },
//         },
//         notchedOutline: {
//           borderColor: 'var(--TextField-brandBorderColor)',
//         },
//       },
//     },
//   },
// });


// const initialFormData = {
//   project_type: '',
//   budget: '',
//   description: '',
//   customer_name: '',
//   customer_number: '',
//   customer_email: '',
// };

// const PopupContent = () => {
//   const outerTheme = useTheme();
//   const [file, setFile] = useState(null);
//   const [notification, setNotification] = useState('');
//   const [formData, setFormData] = useState(initialFormData);

//   const handleInputChange = useCallback((event) => {
//     const { name, value } = event.target;
//     setFormData((prevData) => ({
//       ...prevData,
//       [name]: value,
//     }));
//   }, []);

//   const handleFileChange = useCallback((event) => {
//     const selectedFile = event.target.files[0];
//     if (selectedFile && selectedFile.size > MAX_FILE_SIZE_MB) {
//       setNotification('File size exceeds the 5MB limit.');
//       setFile(null);
//     } else {
//       setNotification(selectedFile ? selectedFile.name : '');
//       setFile(selectedFile);
//     }
//   }, []);

//   const resetForm = () => {
//     setFile(null);
//     setNotification('');
//     setFormData(initialFormData);
//   };

//   const handleSubmit = async (event) => {
//     event.preventDefault();

//     const data = new FormData();
//     Object.entries(formData).forEach(([key, value]) => data.append(key, value));
//     if (file) {
//       data.append('tor_file', file);
//     }

//     try {
//       const response = await axios.post(API_ENDPOINTS.order, data, {
//         headers: { 'Content-Type': 'multipart/form-data' },
//       });

//       if (response.status === 200) {
//         resetForm();
//         console.log('Data submitted successfully');
//       } else {
//         console.error('Failed to submit data:', response.status);
//         setNotification('Failed to submit data. Please try again.');
//       }
//     } catch (error) {
//       console.error('Error:', error);
//     }
//   };

//   return (
//     <div className="popup_container">
//       <h3>Связаться</h3>
//       <form onSubmit={handleSubmit}>
//         <div className="project_type">
//           <p>Тип проекта</p>
//           <OptionSelection
//             options={['Сайт', 'Чат-бот']}
//             name="project_type"
//             value={formData.project_type}
//             onChange={handleInputChange}
//           />
//         </div>
//         <div className="project_budget">
//           <p>Бюджет проекта</p>
//           <OptionSelection
//             options={['50-100 тыс. рублей', '100-300 тыс. рублей', '300-500 тыс. рублей', '500+ тыс. рублей']}
//             name="budget"
//             value={formData.budget}
//             onChange={handleInputChange}
//           />
//         </div>
//         <div className="project_description">
//           <p>Краткое описание проекта</p>
//           <ThemeProvider theme={createCustomTheme(outerTheme)}>
//             <TextField
//               placeholder="Описание"
//               multiline
//               fullWidth
//               name="description"
//               value={formData.description}
//               onChange={handleInputChange}
//             />
//           </ThemeProvider>
//         </div>
//         <div className="project_tor">
//           <p>Техническое задание</p>
//           <div className="input_tor_section">
//             <label className="custom-file-upload">
//               <input type="file" onChange={handleFileChange} />
//               Прикрепить файл с ТЗ
//             </label>
//             <p>{notification}</p>
//           </div>
//         </div>
//         <div className="customer_info">
//           <p>Ваши контактные данные</p>
//           <div className="customer_info_inputs">
//             <input
//               placeholder="Имя"
//               name="customer_name"
//               value={formData.customer_name}
//               onChange={handleInputChange}
//               required
//             />
//             <input
//               placeholder="Номер"
//               type="tel"
//               name="customer_number"
//               value={formData.customer_number}
//               onChange={handleInputChange}
//               required
//             />
//             <input
//               placeholder="Email"
//               type="email"
//               name="customer_email"
//               value={formData.customer_email}
//               onChange={handleInputChange}
//               required
//             />
//           </div>
//         </div>
//         <div className="send_project">
//           <button type="submit">Отправить</button>
//         </div>
//       </form>
//     </div>
//   );
// };

// export default PopupContent;


import { useCallback, useState } from 'react';
import axios from 'axios';
import { createTheme, ThemeProvider, useTheme } from '@mui/material/styles';
import TextField from '@mui/material/TextField';
import { outlinedInputClasses } from '@mui/material/OutlinedInput';
import { API_ENDPOINTS } from '../../apiConfig';
import OptionSelection from './OptionSelection';
import './PopupContent.scss';

// Custom theme for MUI components
const useCustomTheme = (outerTheme) =>
  createTheme({
    palette: {
      mode: outerTheme.palette.mode,
    },
    components: {
      MuiTextField: {
        styleOverrides: {
          root: {
            '--TextField-brandBorderColor': '#E0E3E7',
            '--TextField-brandBorderHoverColor': '#B2BAC2',
            '--TextField-brandBorderFocusedColor': '#6F7E8C',
            '& label.Mui-focused': {
              color: 'var(--TextField-brandBorderFocusedColor)',
            },
          },
        },
      },
      MuiOutlinedInput: {
        styleOverrides: {
          notchedOutline: {
            borderColor: 'var(--TextField-brandBorderColor)',
          },
          root: {
            color: '#fff',
            [`&:hover .${outlinedInputClasses.notchedOutline}`]: {
              borderColor: 'var(--TextField-brandBorderHoverColor)',
            },
            [`&.Mui-focused .${outlinedInputClasses.notchedOutline}`]: {
              borderColor: 'var(--TextField-brandBorderFocusedColor)',
            },
          },
        },
      },
    },
  });

// Component for input fields
const InputField = ({ label, name, value, onChange, required = false, type = 'text' }) => (
  <input
    placeholder={label}
    name={name}
    value={value}
    onChange={onChange}
    required={required}
    type={type}
  />
);

// Component for file upload
const FileUpload = ({ notification, onFileChange }) => (
  <div className="project_tor">
    <div className="input_tor_section">
      <label className="custom-file-upload">
        <input type="file" onChange={onFileChange} />
        Прикрепить файл с ТЗ
      </label>
      <p>{notification}</p>
    </div>
  </div>

);

// Component for the entire form
const Form = ({ formData, handleInputChange, handleFileChange, handleSubmit, fileNotification }) => {
  const outerTheme = useTheme();
  const customTheme = useCustomTheme(outerTheme);

  return (
    <form onSubmit={handleSubmit}>
      <ProjectTypeSelection
        value={formData.project_type}
        onChange={handleInputChange}
      />
      <BudgetSelection
        value={formData.budget}
        onChange={handleInputChange}
      />
      <DescriptionInput
        value={formData.description}
        onChange={handleInputChange}
        customTheme={customTheme}
      />
      <FileUpload
        notification={fileNotification}
        onFileChange={handleFileChange}
      />
      <CustomerInfoInput
        formData={formData}
        handleInputChange={handleInputChange}
      />
      <div className="send_project">
        <button type="submit">Отправить</button>
      </div>
    </form>
  );
};

// PopupContent Component
export default function PopupContent() {
  const [file, setFile] = useState(null);
  const [fileNotification, setFileNotification] = useState(null);
  const [formData, setFormData] = useState({
    project_type: '',
    budget: '',
    description: '',
    customer_name: '',
    customer_number: '',
    customer_email: '',
  });

  const handleInputChange = useCallback((event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  }, []);

  const handleFileChange = useCallback((event) => {
    const selectedFile = event.target.files[0];
    const maxSize = 5 * 1024 * 1024; // 5 MB

    if (selectedFile && selectedFile.size > maxSize) {
      setFileNotification('File size exceeds the 5MB limit.');
      setFile(null);
    } else {
      setFileNotification(selectedFile ? selectedFile.name : null);
      setFile(selectedFile);
    }
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const data = new FormData();
    Object.entries(formData).forEach(([key, value]) => data.append(key, value));
    if (file) data.append('tor_file', file);

    try {
      const response = await axios.post(API_ENDPOINTS.order, data, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.status === 200) {
        resetForm();
        console.log('Data submitted successfully');
      } else {
        console.error('Failed to submit data:', response.status);
        setFileNotification('Failed to submit data. Please try again.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const resetForm = () => {
    setFile(null);
    setFileNotification(null);
    setFormData({
      project_type: '',
      budget: '',
      description: '',
      customer_name: '',
      customer_number: '',
      customer_email: '',
    });
  };

  return (
    <div className="popup_container">
      <h3>Связаться</h3>
      <Form
        formData={formData}
        handleInputChange={handleInputChange}
        handleFileChange={handleFileChange}
        handleSubmit={handleSubmit}
        fileNotification={fileNotification}
      />
    </div>
  );
}

// Sub-components for form sections
const ProjectTypeSelection = ({ value, onChange }) => (
  <div className="project_type">
    <p>Тип проекта</p>
    <OptionSelection
      options={['Сайт', 'Чат-бот']}
      name="project_type"
      value={value}
      onChange={onChange}
      required
    /><br />
  </div>
);

const BudgetSelection = ({ value, onChange }) => (
  <div className="project_budget">
    <p>Бюджет проекта</p>
    <OptionSelection
      options={['50-100 тыс. рублей', '100-300 тыс. рублей', '300-500 тыс. рублей', '500+ тыс. рублей']}
      name="budget"
      value={value}
      onChange={onChange}
      required
      
    /><br />
  </div>
);

const DescriptionInput = ({ value, onChange, customTheme }) => (
  <div className="project_description">
    <p>Краткое описание проекта</p>
    <ThemeProvider theme={customTheme}>
      <TextField
        id="outlined-textarea"
        placeholder="Описание"
        multiline
        sx={{ width: '100%' }}
        name="description"
        value={value}
        onChange={onChange}
      />
    </ThemeProvider>
  </div>
);

const CustomerInfoInput = ({ formData, handleInputChange }) => (
  <div className="customer_info">
    <p>Ваши контактные данные</p>
    <div className="customer_info_inputs">
      <InputField
        label="Имя"
        name="customer_name"
        value={formData.customer_name}
        onChange={handleInputChange}
        required
      />
      <InputField
        label="Номер"
        type="number"
        name="customer_number"
        value={formData.customer_number}
        onChange={handleInputChange}
        required
      />
      <InputField
        label="Email"
        type="email"
        name="customer_email"
        value={formData.customer_email}
        onChange={handleInputChange}
        required
      />
    </div>
  </div>
);
