// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyD6c51vI4ZDldNASfILu0gNV3hHFZ7ZF5o",
  authDomain: "code-summary-a4b33.firebaseapp.com",
  projectId: "code-summary-a4b33",
  storageBucket: "code-summary-a4b33.appspot.com",
  messagingSenderId: "707086011550",
  appId: "1:707086011550:web:d3a3435b26b80f0e627f8f",
  measurementId: "G-XW6M8SNCXE"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export const auth = app.auth();

const provider = new app.auth.GoogleAuthProvider();
provider.setCustomParameters({ prompt: 'select_account' });

export const signInWithGoogle = () => auth.signInWithPopup(provider);