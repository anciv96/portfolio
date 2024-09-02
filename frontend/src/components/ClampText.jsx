import React, { useEffect, useRef } from 'react';
import clamp from 'clamp-js';

const ClampedText = ({ text, lines }) => {
  const textRef = useRef(null);

  useEffect(() => {
    if (textRef.current) {
      clamp(textRef.current, { clamp: lines });
    }
  }, [text, lines]);

  return <p ref={textRef}>{text}</p>;
};

export default ClampedText;
