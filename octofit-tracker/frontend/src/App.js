
import './App.css';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="container mt-4">
        <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4">
          <Link className="navbar-brand" to="/">Octofit Tracker</Link>
          <div className="collapse navbar-collapse">
            <ul className="navbar-nav mr-auto">
              <li className="nav-item"><Link className="nav-link" to="/activities">Activities</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/leaderboard">Leaderboard</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/teams">Teams</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/users">Users</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/workouts">Workouts</Link></li>
            </ul>
          </div>
        </nav>
        <Switch>
          <Route path="/activities" component={Activities} />
          <Route path="/leaderboard" component={Leaderboard} />
          <Route path="/teams" component={Teams} />
          <Route path="/users" component={Users} />
          <Route path="/workouts" component={Workouts} />
          <Route path="/" exact>
            <h2>Bem-vindo ao Octofit Tracker!</h2>
            <p>Escolha uma opção no menu para visualizar os dados.</p>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
