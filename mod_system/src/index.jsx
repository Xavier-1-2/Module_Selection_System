import React, { useState, useEffect } from 'react';
import './style.css';

function Index() {
  const [modules, setModules] = useState([]);
  const [allModules, setAllModules] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/modules')
      .then((res) => res.json())
      .then((data) => setAllModules(data))
      .catch((err) => console.error(err));

    fetch('http://127.0.0.1:5000/selected_modules')
      .then((res) => res.json())
      .then((data) => setModules(data))
      .catch((err) => console.error(err));
  }, []);

 const handleAddModule = async (moduleToAdd) => {
  try {
    const res = await fetch('http://127.0.0.1:5000/modules', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ...moduleToAdd,
        student_id: "student_123"
      })
    });

    const addedModule = await res.json();

    if (!res.ok) {
      alert(addedModule.message || 'Time clash detected!');
      return;
    }

    setModules([...modules, addedModule]); //  add new module directly

  } catch (err) {
    console.error(err);
  }
};



  const handleRemoveModule = async (moduleCode) => {
  try {
    const res = await fetch(`http://127.0.0.1:5000/selected_modules/${moduleCode}`, {
      method: 'DELETE',
    });

    const result = await res.json();
    if (!res.ok) {
      alert(result.message || 'Failed to remove module');
      return;
    }

    // Update frontend state properly
    setModules(modules.filter((mod) => mod.id !== moduleCode));
  } catch (err) {
    console.error(err);
  }
};


  const renderModulesByTime = (timePeriod) =>
    allModules
      .filter((mod) => mod.time_period === timePeriod)
      .map((mod) => (
        <div key={mod.id} className="module-card">
          <div className="module-info">
            <p className="module-name">{mod.name}</p>
            <small className="module-time">
              {mod.start_time} - {mod.end_time}
            </small>
          </div>
          <button className="add-btn" onClick={() => handleAddModule(mod)}>
            Add
          </button>
        </div>
      ));

  // Timetable Section
  const renderTimetable = () => {
    // Sort by start time for visual order
    const sortedModules = [...modules].sort(
      (a, b) =>
        new Date(`1970/01/01 ${a.start_time}`) -
        new Date(`1970/01/01 ${b.start_time}`)
    );

    return (
      <div className="timetable">
        <h2>Your Timetable</h2>
        {sortedModules.length === 0 ? (
          <p className="empty-text">No modules selected yet.</p>
        ) : (
          <table className="timetable-table">
            <thead>
              <tr>
                <th>Module</th>
                <th>Time</th>
                <th>Occurrence</th>
                <th>Faculty</th>
              </tr>
            </thead>
            <tbody>
              {sortedModules.map((mod) => (
                <tr key={mod.id}>
                  <td>{mod.name}</td>
                  <td>
                    {mod.start_time} - {mod.end_time}
                  </td>
                  <td>{mod.occurrence}</td>
                  <td>{mod.faculty}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    );
  };

  return (
    <div className="container">
      <header className="main-title">
        <h1>Module Selection System</h1>
      </header>

      <nav className="navbar">
        <button className="nav-btn active">Student</button>
        <button className="nav-btn">Admin</button>
      </nav>

      <div className="modules-grid">
        <div className="module-section">
          <h2>Morning Modules</h2>
          <div className="module-list">{renderModulesByTime('Morning')}</div>
        </div>

        <div className="module-section">
          <h2>Afternoon Modules</h2>
          <div className="module-list">{renderModulesByTime('Afternoon')}</div>
        </div>

        <div className="module-section">
          <h2>Evening Modules</h2>
          <div className="module-list">{renderModulesByTime('Evening')}</div>
        </div>

        <div className="selected-section">
          <h2>Selected Modules</h2>
          {modules.length === 0 ? (
            <p className="empty-text">No modules selected yet.</p>
          ) : (
            modules.map((mod) => (
              <div key={mod.id} className="module-card selected">
                <div className="module-info">
                  <p className="module-name">{mod.name}</p>
                  <small className="module-time">
                    {mod.start_time} - {mod.end_time}
                  </small>
                </div>
                <button
                  className="remove-btn"
                  onClick={() => handleRemoveModule(mod.id)}
                >
                  Remove
                </button>
              </div>
            ))
          )}
        </div>
      </div>

    
      {renderTimetable()}
    </div>
  );
}

export default Index;
