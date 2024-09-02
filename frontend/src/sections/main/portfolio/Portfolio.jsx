import axios from 'axios';

import * as React from 'react';
import PropTypes from 'prop-types';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import { useEffect } from 'react';

import './Portfolio.scss'
import { API_ENDPOINTS } from '../../../apiConfig'
import ClampedText from '../../../components/ClampText';

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`vertical-tabpanel-${index}`}
      aria-labelledby={`vertical-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
};

function a11yProps(index) {
  return {
    id: `vertical-tab-${index}`,
    'aria-controls': `vertical-tabpanel-${index}`,
  };
}

const Project = ({project}) => {
    console.log(project)
    return(
        <div className='project_item'>
            <a href={project.url}>
              <img src={project.image_path} alt="site_photo" />
            </a>
            <h3>{project.title}</h3>
              <ClampedText 
                text={project.description}
                lines={10}
              />
        </div>
    )
}

export default function Portfolio() {
  const [value, setValue] = React.useState(0);
  const [projects, setProjects] = React.useState([])
  
  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  useEffect(() => {
      axios.get(API_ENDPOINTS.projects)
      .then(response => {
          setProjects(response.data)
      })
      .catch(error => {
          console.log('Error fetching projects:', error)
      })
  }, [])

  return (
    <div className="main__portfolio" id="portfolio" style={{ scrollMarginTop: "10rem" }}>
        <h2>Portfolio</h2>
        <Box className='main__portfolio_content'>
            <Box className='portfolio_projects'>
                {
                  projects.map((project, id) => (
                    <TabPanel value={value} index={id} key={id}>
                      <Project 
                        project={project}
                      />
                    </TabPanel>
                  ))
                }
            </Box>
            <Tabs
                orientation="vertical"
                variant="scrollable"
                value={value}
                onChange={handleChange}
                aria-label="Vertical tabs example"
                className='portfolio_tabs_menu'
                indicatorColor="inherit"
            >
              {
                projects.map((project, id) => (
                  <Tab label={project.title} {...a11yProps(id)} className='portfolio_tab' key={id}/>
                ))
              }
        </Tabs>
        </Box>
    </div>
  );
}
