import "../App.css";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-inner">

        <div className="navbar-brand">
          <div className="navbar-logo">CP</div>
          <span className="navbar-title">Churn Predictor</span>
        </div>

        <div className="navbar-badge">
          <span className="navbar-badge-dot"></span>
          ML Model Active
        </div>

      </div>
    </nav>
  );
}

export default Navbar;