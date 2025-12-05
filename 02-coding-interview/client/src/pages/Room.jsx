import React, { useEffect, useState, useRef } from 'react';
import { useParams } from 'react-router-dom';
import CodeMirror from '@uiw/react-codemirror';
import { javascript } from '@codemirror/lang-javascript';
import { python } from '@codemirror/lang-python';
import io from 'socket.io-client';

const Room = () => {
  const { roomId } = useParams();
  const [code, setCode] = useState("// Start coding here...");
  const [language, setLanguage] = useState("javascript");
  const socketRef = useRef(null);

  useEffect(() => {
    // Connect to backend
    socketRef.current = io('http://localhost:3001');
    
    socketRef.current.emit('join_room', roomId);

    socketRef.current.on('receive_code', (newCode) => {
      setCode(newCode);
    });

    socketRef.current.on('receive_language', (newLang) => {
      setLanguage(newLang);
    });

    return () => {
      socketRef.current.disconnect();
    };
  }, [roomId]);

  const handleCodeChange = (value) => {
    setCode(value);
    if (socketRef.current) {
        socketRef.current.emit('code_change', { roomId, code: value });
    }
  };

  const handleLanguageChange = (e) => {
    const newLang = e.target.value;
    setLanguage(newLang);
    if (socketRef.current) {
        socketRef.current.emit('language_change', { roomId, language: newLang });
    }
  };

  const getExtensions = () => {
    if (language === 'python') return [python()];
    return [javascript({ jsx: true })];
  };

  const executeCode = () => {
    console.log("Executing code:", code);
    alert("Code execution result will be shown here (check console for now).");
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Interview Room: {roomId}</h2>
      <div style={{ marginBottom: '10px', display: 'flex', gap: '10px' }}>
        <select value={language} onChange={handleLanguageChange} style={{ padding: '5px' }}>
          <option value="javascript">JavaScript</option>
          <option value="python">Python</option>
        </select>
        <button onClick={executeCode} style={{ padding: '5px 10px', cursor: 'pointer' }}>
          Run Code
        </button>
      </div>
      <div style={{ border: '1px solid #ccc' }}>
        <CodeMirror
            value={code}
            height="500px"
            extensions={getExtensions()}
            onChange={handleCodeChange}
            theme="dark"
        />
      </div>
    </div>
  );
};

export default Room;
