import { useState } from 'react';
import { Box } from '@chakra-ui/react';
import { Wheel } from './types';
import RollScreen from './features/roll/RollScreen';
import Dashboard from './features/dashboard/Dashboard';
import PWAReloadPrompt from './components/PWAReloadPrompt';

function App() {
  const [activeWheel, setActiveWheel] = useState<Wheel | null>(null);

  return (
    <Box>
      {activeWheel ? (
        <RollScreen wheel={activeWheel} onBack={() => setActiveWheel(null)} />
      ) : (
        <Dashboard onStartWheel={setActiveWheel} />
      )}
      <PWAReloadPrompt />
    </Box>
  );
}

export default App;