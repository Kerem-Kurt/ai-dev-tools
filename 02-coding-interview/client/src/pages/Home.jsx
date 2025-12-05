import React from 'react';
import { useNavigate } from 'react-router-dom';
import { v4 as uuidv4 } from 'uuid';

const Home = () => {
  const navigate = useNavigate();

  const createRoom = () => {
    const id = uuidv4();
    navigate(`/room/${id}`);
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      <button onClick={createRoom} style={{ padding: '10px 20px', fontSize: '1.2em', cursor: 'pointer' }}>
        Create New Interview Room
      </button>
    </div>
  );
};

export default Home;
