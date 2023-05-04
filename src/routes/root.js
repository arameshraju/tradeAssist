import { Outlet } from "react-router-dom";

export default function Root() {
    return (
      <>
        <div id="sidebar">
          <h1>Options</h1>
          <nav>
            <ul>
              <li>
                <a href={`/payoff`}>Payoff Graph</a>
              </li>
              <li>
                <a href={`/option-chain`}>Option Chain</a>
              </li>
              <li>
                <a href={`/chart`}>Chart</a>
              </li>
            </ul>
          </nav>
        </div>
        <div id="detail">
        <Outlet />
        </div>
      </>
    );
  }