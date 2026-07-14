import "../App.css";

function Footer() {
  return (
    <footer className="app-footer">
      <div className="footer-inner">
        <p className="footer-text">
          Built with ❤️ using
          <span className="footer-tech"> React</span> •
          <span className="footer-tech"> FastAPI</span> •
          <span className="footer-tech"> Scikit-Learn</span> •
          <span className="footer-tech"> Docker</span>
        </p>
        <p className="footer-copyright">
          © {new Date().getFullYear()} Customer Churn Predictor
        </p>
      </div>
    </footer>
  );
}

export default Footer;