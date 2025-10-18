import { use } from 'react'
import './style.css'

function Index(){
    const [modules, setmodules] = useState([])

    const HandleModules = () => {
        setmodules([...modules, { name: `Module ${modules.length + 1}` }]);
    };
    
    return(
        
       < div>
        
        <header className='main_title'>
            <h1>Module Selection System</h1>
        </header>

        <nav className='Navi'>
            <h4>Student</h4>
            <h4>Admin</h4>
        </nav>

        <div className='SearchBar'>
            <input type="text" placeholder='Search' />
        </div>
        <br />
        
        <div className='main_module_sel_section'>
            <div className='Module_Data'><p>Module Name</p> <button>Add</button></div>
        </div>
        </div>
         
    );
};

export default Index