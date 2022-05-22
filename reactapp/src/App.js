import logo from './logo.svg';
import './App.css';
import { realm } from './config';
import { Switch } from 'react-router';
import AppIndex from './apps';
import { ReactKeycloakProvider } from '@react-keycloak/web';
import keycloak, { keycloakConfig } from './apps/module/keycloak.config';


function App() {
  return (
    // <ReactKeycloakProvider
    //   authClient={keycloak}
    //   // initOptions={{ onLoad: 'login-required', pkceMethod: 'S256' }}
    // >
      <AppIndex />
    // </ReactKeycloakProvider>
  );
}

export default App;
