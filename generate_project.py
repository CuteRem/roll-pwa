import os
import sys

PROJECT_NAME = "roll-pwa"

# 定义项目文件结构和内容
project_structure = {
    "index.html": """
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>肉店大师</title>
    <meta name="description" content="一个帮你快速做出决策的工具">
    
    <link rel="manifest" href="./manifest.webmanifest">
    <link rel="icon" href="./favicon.ico">
    <link rel="apple-touch-icon" href="./apple-touch-icon.png" sizes="180x180">
    <meta name="theme-color" content="#5A67D8">
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
""",
    "package.json": """
{
  "name": "roll-pwa",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite --host",
    "build": "tsc && vite build",
    "preview": "vite preview --host"
  },
  "dependencies": {
    "@chakra-ui/react": "^2.8.2",
    "@emotion/react": "^11.11.4",
    "@emotion/styled": "^11.11.5",
    "framer-motion": "^11.1.7",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-icons": "^5.2.0",
    "uuid": "^9.0.1"
  },
  "devDependencies": {
    "@types/react": "^18.2.66",
    "@types/react-dom": "^18.2.22",
    "@types/uuid": "^9.0.8",
    "@vitejs/plugin-react": "^4.2.1",
    "typescript": "^5.2.2",
    "vite": "^5.2.0",
    "vite-plugin-pwa": "^0.19.8"
  }
}
""",
    "vite.config.ts": """
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { VitePWA } from 'vite-plugin-pwa';

export default defineConfig({
  base: './',
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.ico', 'apple-touch-icon.png', 'pwa-192x192.png', 'pwa-512x512.png', 'maskable-icon-512x512.png'],
      manifest: {
        name: '肉店大师',
        short_name: '肉店大师',
        description: '一个帮你快速做出决策的工具',
        theme_color: '#5A67D8',
        background_color: '#ffffff',
        display: 'standalone',
        start_url: '.',
        icons: [
          {
            src: 'pwa-192x192.png',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: 'pwa-512x512.png',
            sizes: '512x512',
            type: 'image/png'
          },
          {
            src: 'maskable-icon-512x512.png',
            sizes: '512x512',
            type: 'image/png',
            purpose: 'maskable'
          }
        ]
      }
    })
  ],
  server: {
    host: true
  },
  preview: {
    host: true
  }
});
""",
    "tsconfig.json": """
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable", "WebWorker"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "types": ["vite-plugin-pwa/client"]
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
""",
    "tsconfig.node.json": """
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}
""",
    "src/main.tsx": """
import React from 'react';
import ReactDOM from 'react-dom/client';
import { ChakraProvider, ColorModeScript } from '@chakra-ui/react';
import App from './App';
import theme from './theme';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <ChakraProvider theme={theme}>
      <ColorModeScript initialColorMode={theme.config.initialColorMode} />
      <App />
    </ChakraProvider>
  </React.StrictMode>
);
""",
    "src/App.tsx": """
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
""",
    "src/theme.ts": """
import { extendTheme, type ThemeConfig } from '@chakra-ui/react';
import { mode } from '@chakra-ui/theme-tools';

const config: ThemeConfig = {
  initialColorMode: 'system',
  useSystemColorMode: true,
};

const theme = extendTheme({
  config,
  colors: {
    brand: {
      50: '#EBF8FF',
      100: '#C3DAFE',
      200: '#A3BFFA',
      300: '#7F9CF5',
      400: '#667EEA',
      500: '#5A67D8',
      600: '#4C51BF',
      700: '#434190',
      800: '#3C366B',
      900: '#322F5A',
    },
  },
  styles: {
    global: (props: any) => ({
      'body': {
        bg: mode('gray.50', 'gray.900')(props),
        color: mode('gray.800', 'whiteAlpha.900')(props),
        lineHeight: 'base',
      },
    }),
  },
});

export default theme;
""",
    "src/types/index.ts": """
export interface WheelOption {
  text: string;
}

export interface Wheel {
  id: string;
  title: string;
  type: 'custom' | 'number';
  options: WheelOption[];
  min?: number;
  max?: number;
}
""",
    "src/features/dashboard/Dashboard.tsx": """
import { Box, Container, VStack } from '@chakra-ui/react';
import Header from '../../components/Header';
import QuickRoll from './QuickRoll';
import { Wheel } from '../../types';

interface DashboardProps {
    onStartWheel: (wheel: Wheel) => void;
}

const Dashboard = ({ onStartWheel }: DashboardProps) => {
    return (
        <Box>
            <Header />
            <Container maxW="container.lg" py={{base: 6, md: 10}}>
                <VStack spacing={8} align="stretch">
                    <QuickRoll onStartWheel={onStartWheel} />
                </VStack>
            </Container>
        </Box>
    );
};

export default Dashboard;
""",
    "src/features/dashboard/QuickRoll.tsx": """
import { useState } from 'react';
import { Box, Heading, VStack, Tabs, TabList, Tab, TabPanels, TabPanel, Textarea, Button, HStack, NumberInput, NumberInputField, Text, useToast, Icon, useColorModeValue, useDisclosure, Input, FormControl } from '@chakra-ui/react';
import { v4 as uuidv4 } from 'uuid';
import { Wheel } from '../../types';
import { FaBolt, FaDice, FaQuestion, FaCoins } from 'react-icons/fa';
import DecisionModal from '../../components/DecisionModal';

type DecisionType = 'yesno' | 'coin';

interface QuickRollProps {
    onStartWheel: (wheel: Wheel) => void;
}

const QuickRoll = ({ onStartWheel }: QuickRollProps) => {
    const [title, setTitle] = useState('');
    const [customOptions, setCustomOptions] = useState('选项A\\n选项B\\n选项C');
    const [min, setMin] = useState<number | string>(1);
    const [max, setMax] = useState<number | string>(100);
    const [decisionType, setDecisionType] = useState<DecisionType | null>(null);
    const [modalTitle, setModalTitle] = useState('');
    const { isOpen, onOpen, onClose } = useDisclosure();
    const toast = useToast();
    const bgColor = useColorModeValue('white', 'gray.800');

    const handleNumberChange = (setter: React.Dispatch<React.SetStateAction<number | string>>) => (valueAsString: string, valueAsNumber: number) => {
        setter(valueAsString === '' ? '' : valueAsNumber);
    };

    const handleTemplatedRoll = (type: DecisionType) => {
        const finalTitle = title.trim();
        const defaultTitles = {
            yesno: "是非决策",
            coin: "抛硬币"
        };
        setModalTitle(finalTitle || defaultTitles[type]);
        setDecisionType(type);
        onOpen();
    };
    
    const handleWheelRoll = (type: 'custom' | 'number') => {
        let wheel: Wheel | null = null;
        const finalTitle = title.trim();

        if (type === 'custom') {
            const options = customOptions.split(/[\\n,，]/).map(s => s.trim()).filter(Boolean);
            if (options.length < 2) {
                toast({ title: "自定义模式至少需要2个选项", status: 'warning', duration: 2000, position: 'top' });
                return;
            }
            wheel = { id: uuidv4(), title: finalTitle || '自定义决策', type: 'custom', options: options.map(text => ({ text })) };
        } else if (type === 'number') {
            const minNum = typeof min === 'number' ? min : parseInt(String(min), 10);
            const maxNum = typeof max === 'number' ? max : parseInt(String(max), 10);

            if (isNaN(minNum) || isNaN(maxNum)) {
                toast({ title: "请输入有效的数字", status: 'warning', duration: 2000, position: 'top' });
                return;
            }

            if (minNum >= maxNum) {
                toast({ title: "最大值必须大于最小值", status: 'warning', duration: 2000, position: 'top' });
                return;
            }
             wheel = { id: uuidv4(), title: finalTitle || `数字决策 (${minNum}-${maxNum})`, type: 'number', min: minNum, max: maxNum, options: [] };
        }
        
        if(wheel) {
            onStartWheel(wheel);
        }
    };


    return (
        <>
            <Box borderWidth="1px" borderRadius="xl" p={{base: 4, md: 6}} boxShadow="lg" bg={bgColor}>
                <VStack spacing={4} align="stretch">
                    <HStack>
                        <Icon as={FaBolt} w={6} h={6} color="yellow.400" />
                        <Heading size="lg">快速决策</Heading>
                    </HStack>
                    <FormControl>
                        <Input 
                            variant="flushed" 
                            placeholder="选填：为你的决策取个响亮的名字吧！"
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                        />
                    </FormControl>
                </VStack>
                
                <Tabs isFitted variant="soft-rounded" colorScheme="brand" mt={4}>
                    <TabList>
                        <Tab>数字</Tab>
                        <Tab>是非</Tab>
                        <Tab>硬币</Tab>
                        <Tab>自定义</Tab>
                    </TabList>
                    <TabPanels mt={4}>
                        <TabPanel>
                             <VStack spacing={4}>
                                <HStack spacing={4} w="full" justify="center">
                                   <Text>从</Text>
                                   <NumberInput value={min} onChange={handleNumberChange(setMin)} maxW="120px"><NumberInputField /></NumberInput>
                                   <Text>到</Text>
                                   <NumberInput value={max} onChange={handleNumberChange(setMax)} maxW="120px"><NumberInputField /></NumberInput>
                                </HStack>
                                <Button colorScheme="brand" onClick={() => handleWheelRoll('number')} leftIcon={<FaDice />}>开始滚动</Button>
                            </VStack>
                        </TabPanel>
                        <TabPanel>
                            <VStack spacing={4}>
                                <Text>点击下方按钮进行是非决策</Text>
                                <Button colorScheme="brand" onClick={() => handleTemplatedRoll('yesno')} leftIcon={<FaQuestion />}>开始</Button>
                            </VStack>
                        </TabPanel>
                        <TabPanel>
                            <VStack spacing={4}>
                                <Text>点击下方按钮抛硬币</Text>
                                <Button colorScheme="brand" onClick={() => handleTemplatedRoll('coin')} leftIcon={<FaCoins />}>抛硬币</Button>
                            </VStack>
                        </TabPanel>
                        <TabPanel>
                             <VStack spacing={4}>
                                <Textarea 
                                    placeholder="输入选项，每行一个或用逗号隔开"
                                    value={customOptions}
                                    onChange={e => setCustomOptions(e.target.value)}
                                    rows={5}
                                />
                                <Button colorScheme="brand" onClick={() => handleWheelRoll('custom')} alignSelf="flex-end" leftIcon={<FaDice />}>开始滚动</Button>
                            </VStack>
                        </TabPanel>
                    </TabPanels>
                </Tabs>
            </Box>
            <DecisionModal type={decisionType} title={modalTitle} isOpen={isOpen} onClose={onClose} />
        </>
    );
};

export default QuickRoll;
""",
    "src/features/roll/RollScreen.tsx": """
import { useState } from 'react';
import { Button, Heading, VStack, IconButton, useColorModeValue } from '@chakra-ui/react';
import { FaArrowLeft } from 'react-icons/fa';
import { Wheel } from '../../types';
import SlotMachine from './SlotMachine';

interface RollScreenProps {
  wheel: Wheel;
  onBack: () => void;
}

const RollScreen = ({ wheel, onBack }: RollScreenProps) => {
  const [isSpinning, setIsSpinning] = useState(false);
  const [result, setResult] = useState<string | null>(null);
  const bgColor = useColorModeValue('gray.100', 'gray.800');

  const getOptions = () => {
    if (wheel.type === 'number') {
      const options = [];
      const min = wheel.min ?? 1;
      const max = wheel.max ?? 100;
      for (let i = min; i <= max; i++) {
        options.push({ text: i.toString() });
      }
      return options;
    }
    return wheel.options;
  };
  
  const options = getOptions();

  const handleSpin = () => {
    if (isSpinning) return;
    setResult(null); // Reset result before spinning
    setIsSpinning(true);
  };

  const handleSpinComplete = (finalResult: string) => {
    setResult(finalResult);
    setIsSpinning(false);
  };

  return (
    <VStack minH="100vh" p={4} spacing={8} justify="center" overflowX="hidden" bg={bgColor}>
        <IconButton 
            aria-label="Back" 
            icon={<FaArrowLeft />} 
            onClick={onBack} 
            isRound 
            position="absolute" top={6} left={6}
            size="lg"
            variant="ghost"
        />

        <Heading as="h1" size="2xl" textAlign="center" px={{base: 4, md: 16}}>
          {wheel.title}
        </Heading>
        
        <SlotMachine
            options={options.map(o => o.text)}
            isSpinning={isSpinning}
            onComplete={handleSpinComplete}
        />

        <Button
          colorScheme="brand"
          size="lg"
          onClick={handleSpin}
          isLoading={isSpinning}
          loadingText="滚动中..."
          px={16}
          py={8}
          fontSize="2xl"
          boxShadow="lg"
          rounded="full"
          isDisabled={isSpinning}
        >
          {result ? "再来一次" : "开始滚动"}
        </Button>
    </VStack>
  );
};

export default RollScreen;
""",
    "src/features/roll/SlotMachine.tsx": """
import { Box, Text, useColorModeValue } from '@chakra-ui/react';
import { motion, useAnimate } from 'framer-motion';
import { useEffect, useMemo, useRef } from 'react';

interface SlotMachineProps {
  options: string[];
  isSpinning: boolean;
  onComplete: (result: string) => void;
}

const ITEM_HEIGHT = 80; // Height of each option item in pixels

const SlotMachine = ({ options, isSpinning, onComplete }: SlotMachineProps) => {
  const [scope, animate] = useAnimate();
  const bgColor = useColorModeValue('gray.200', 'gray.700');
  const highlightColor = useColorModeValue('brand.500', 'brand.300');

  const animationList = useMemo(() => {
      if (options.length === 0) return [];
      const repeats = Math.max(5, Math.ceil(50 / options.length));
      return Array(repeats).fill(options).flat();
  }, [options]);

  const onCompleteRef = useRef(onComplete);
  onCompleteRef.current = onComplete;

  useEffect(() => {
    const startAnimation = async () => {
      if (isSpinning && scope.current && options.length > 0) {
        const newResultIndex = Math.floor(Math.random() * options.length);
        
        const totalRepeats = Math.max(5, Math.ceil(50 / options.length));
        const targetRepeatIndex = totalRepeats - 2; 
        const targetY = -((targetRepeatIndex * options.length) + newResultIndex) * ITEM_HEIGHT;

        await animate(scope.current, { y: 0 }, { duration: 0 });

        await animate(
          scope.current,
          { y: targetY },
          {
            duration: 3,
            ease: 'circOut',
          }
        );
        onCompleteRef.current(options[newResultIndex]);
      }
    };
    startAnimation();
  }, [isSpinning]);

  return (
    <Box
      w={{ base: '90%', md: '500px' }}
      h={`${ITEM_HEIGHT}px`}
      bg={bgColor}
      borderRadius="lg"
      overflow="hidden"
      position="relative"
      boxShadow="inner"
      _after={{
        content: '""',
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        zIndex: 3,
        bgGradient: `linear(to-b, ${bgColor}, transparent 30%, transparent 70%, ${bgColor})`,
        pointerEvents: 'none',
      }}
    >
      <Box 
        position="absolute"
        top="0"
        left="0"
        right="0"
        h="100%"
        zIndex={2}
        borderY="2px solid"
        borderColor={highlightColor}
        pointerEvents="none"
      />
      <motion.div ref={scope}>
        {animationList.map((option, i) => (
          <Text
            key={`${option}-${i}`}
            h={`${ITEM_HEIGHT}px`}
            lineHeight={`${ITEM_HEIGHT}px`}
            textAlign="center"
            fontSize="4xl"
            fontWeight="bold"
            isTruncated
            px={4}
          >
            {option}
          </Text>
        ))}
      </motion.div>
    </Box>
  );
};

export default SlotMachine;
""",
    "src/components/Header.tsx": """
import { Box, Flex, Heading, Spacer, useColorMode, IconButton, useColorModeValue } from '@chakra-ui/react';
import { FaSun, FaMoon } from 'react-icons/fa';

const Header = () => {
  const { colorMode, toggleColorMode } = useColorMode();
  const bg = useColorModeValue('rgba(255, 255, 255, 0.8)', 'rgba(23, 25, 35, 0.8)');

  return (
    <Box
      as="header"
      bg={bg}
      py={3}
      px={{ base: 4, md: 8 }}
      boxShadow="sm"
      position="sticky"
      top={0}
      zIndex="sticky"
      backdropFilter="saturate(180%) blur(5px)"
    >
      <Flex align="center" maxW="container.lg" mx="auto">
        <Heading as="h1" size="lg" letterSpacing="tight">
          肉店大师
        </Heading>
        <Spacer />
        <IconButton
          aria-label="Toggle theme"
          icon={colorMode === 'dark' ? <FaSun /> : <FaMoon />}
          onClick={toggleColorMode}
          isRound
          variant="ghost"
        />
      </Flex>
    </Box>
  );
};

export default Header;
""",
    "src/components/DecisionModal.tsx": """
import { Modal, ModalOverlay, ModalContent, ModalHeader, ModalCloseButton, ModalBody } from "@chakra-ui/react"
import CoinToss from "./CoinToss";
import YesNoResult from "./YesNoResult";

interface DecisionModalProps {
    type: 'yesno' | 'coin' | null;
    title: string;
    isOpen: boolean;
    onClose: () => void;
}

const DecisionModal = ({ type, title, isOpen, onClose }: DecisionModalProps) => {
    const modalBodyMinHeight = "280px";

    return (
        <Modal isOpen={isOpen} onClose={onClose} isCentered size="md" motionPreset="slideInBottom">
            <ModalOverlay bg='blackAlpha.600' backdropFilter='blur(5px)' />
            <ModalContent mx={4} borderRadius="xl">
                <ModalHeader textAlign="center">{title}</ModalHeader>
                <ModalCloseButton />
                <ModalBody minH={modalBodyMinHeight} display="flex" alignItems="center" justifyContent="center">
                    {type === 'yesno' && <YesNoResult key={isOpen ? 'yesno-open' : 'yesno-closed'} />}
                    {type === 'coin' && <CoinToss key={isOpen ? 'coin-open' : 'coin-closed'} />}
                </ModalBody>
            </ModalContent>
        </Modal>
    );
};

export default DecisionModal;
""",
    "src/components/YesNoResult.tsx": """
import { useState } from "react";
import { Box, Icon, Text, Button, VStack } from "@chakra-ui/react";
import { motion, AnimatePresence } from "framer-motion";
import { FaCheck, FaTimes, FaQuestion } from "react-icons/fa";

const symbols = [
    { icon: FaCheck, color: "green.400" },
    { icon: FaTimes, color: "red.400" },
];

const YesNoResult = () => {
    const [isDeciding, setIsDeciding] = useState(false);
    const [result, setResult] = useState<{ icon: any, color: string } | null>(null);

    const handleDecide = () => {
        if(isDeciding) return;
        setResult(null);
        setIsDeciding(true);
        const decisionTimeout = setTimeout(() => {
            const finalResult = Math.random() < 0.5 ? symbols[0] : symbols[1];
            setResult(finalResult);
            setIsDeciding(false);
        }, 1500);

        return () => clearTimeout(decisionTimeout);
    };

    return (
        <VStack spacing={8} w="full">
            <Box textAlign="center" w="full" h="150px" display="flex" flexDirection="column" alignItems="center" justifyContent="center">
                <AnimatePresence mode="wait">
                    {!result && !isDeciding && (
                         <motion.div
                            key="initial"
                            initial={{ opacity: 0, scale: 0.8 }}
                            animate={{ opacity: 1, scale: 1 }}
                            exit={{ opacity: 0, scale: 0.8 }}
                        >
                            <Icon as={FaQuestion} boxSize="100px" color="gray.500" />
                        </motion.div>
                    )}
                    {isDeciding && (
                        <motion.div
                            key="deciding"
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0, transition: { repeat: Infinity, duration: 0.5, repeatType: 'reverse', ease: 'easeInOut' } }}
                            exit={{ opacity: 0, scale: 0.5 }}
                        >
                            <Text fontSize="xl">正在判断...</Text>
                        </motion.div>
                    )}
                   {result && !isDeciding && (
                     <motion.div
                        key="result"
                        initial={{ scale: 0.5, opacity: 0 }}
                        animate={{ scale: 1, opacity: 1, transition: { type: 'spring', stiffness: 300, damping: 20 } }}
                     >
                        <Icon as={result.icon} boxSize="150px" color={result.color} />
                    </motion.div>
                   )}
                </AnimatePresence>
            </Box>
            <Button onClick={handleDecide} isLoading={isDeciding} colorScheme="brand" isDisabled={isDeciding}>
                {result ? "再来一次" : "开始"}
            </Button>
        </VStack>
    );
};

export default YesNoResult;
""",
    "src/components/CoinToss.tsx": """
import { useState } from 'react';
import { Box, Button, VStack, Icon } from "@chakra-ui/react";
import { motion, AnimatePresence } from 'framer-motion';
import { GiGinkgoLeaf } from "react-icons/gi";
import { RiCopperCoinLine } from 'react-icons/ri';

const CoinFace = ({ faceType }: { faceType: 'heads' | 'tails' }) => {
    const isHeads = faceType === 'heads';
    const bg = isHeads
        ? "linear-gradient(45deg, #fde08d, #f8b500)"
        : "linear-gradient(45deg, #e0e0e0, #a9a9a9)";
    const icon = isHeads ? GiGinkgoLeaf : RiCopperCoinLine;

    return (
        <motion.div
            key={faceType}
            initial={{ rotateY: -90, opacity: 0 }}
            animate={{ rotateY: 0, opacity: 1 }}
            exit={{ rotateY: 90, opacity: 0 }}
            transition={{ duration: 0.2, ease: 'easeInOut' }}
            style={{
                position: 'absolute',
                width: '100%',
                height: '100%',
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                background: bg,
                boxShadow: "inset 0 0 20px rgba(0,0,0,0.3)"
            }}
        >
            <Icon as={icon} w={20} h={20} color="whiteAlpha.900" filter="drop-shadow(0 0 5px rgba(0,0,0,0.5))" />
        </motion.div>
    );
};


const CoinToss = () => {
    const [isFlipping, setIsFlipping] = useState(false);
    const [visibleFace, setVisibleFace] = useState<'heads' | 'tails'>('heads');
    const [result, setResult] = useState<'heads' | 'tails' | null>(null);

    const handleFlip = () => {
        if (isFlipping) return;
        setIsFlipping(true);
        setResult(null);
        const outcome = Math.random() < 0.5 ? 'heads' : 'tails';
        
        let flipCount = 0;
        const totalFlips = 10;
        const flipInterval = setInterval(() => {
            setVisibleFace(prev => (prev === 'heads' ? 'tails' : 'heads'));
            flipCount++;
            if (flipCount >= totalFlips) {
                clearInterval(flipInterval);
                setVisibleFace(outcome);
                setResult(outcome);
                setIsFlipping(false);
            }
        }, 120);
    };

    return (
        <VStack spacing={8}>
            <Box w="150px" h="150px" style={{ perspective: '1000px' }} onClick={handleFlip} cursor="pointer">
                <Box w="full" h="full" position="relative">
                   <AnimatePresence>
                       <CoinFace faceType={visibleFace} />
                   </AnimatePresence>
                </Box>
            </Box>
            <Button onClick={handleFlip} isLoading={isFlipping} colorScheme="brand" isDisabled={isFlipping}>
                {result ? "再来一次" : "开始"}
            </Button>
        </VStack>
    );
};

export default CoinToss;
""",
    "src/components/PWAReloadPrompt.tsx": """
import {
  Box,
  Button,
  Slide,
  useDisclosure,
  useColorModeValue,
  Text,
  HStack,
} from '@chakra-ui/react';
import { useRegisterSW } from 'virtual:pwa-register/react';

function PWAReloadPrompt() {
  const {
    needRefresh: [needRefresh],
    updateServiceWorker,
  } = useRegisterSW({
    onRegistered(r) {
      console.log(`SW Registered: ${r}`);
    },
    onRegisterError(error) {
      console.log('SW registration error', error);
    },
  });

  const { isOpen, onClose } = useDisclosure({ defaultIsOpen: needRefresh });

  const bg = useColorModeValue('white', 'gray.700');
  const textColor = useColorModeValue('gray.800', 'white');

  if (!isOpen) {
      return null;
  }

  return (
    <Box position="fixed" bottom="0" left="0" right="0" p={4} zIndex="overlay">
        <Slide direction="bottom" in={isOpen} style={{ zIndex: 10 }}>
        <Box
            p="4"
            color={textColor}
            bg={bg}
            shadow="lg"
            textAlign="center"
            borderRadius="md"
        >
            <HStack justify="center" spacing={4}>
            <Text>有新版本可用！</Text>
            <Button
                colorScheme="brand"
                onClick={() => updateServiceWorker(true)}
            >
                刷新
            </Button>
            <Button variant="ghost" onClick={onClose}>
                关闭
            </Button>
            </HStack>
        </Box>
        </Slide>
    </Box>
  );
}

export default PWAReloadPrompt;
"""
}

def create_project(base_path, project_name):
    """Creates the project structure and files inside a dedicated folder."""
    
    project_root = os.path.join(base_path, project_name)
    
    if not os.path.exists(project_root):
        os.makedirs(project_root)
        print(f"✅ Created project directory: {project_root}")
    else:
        print(f"⚠️ Project directory '{project_root}' already exists. Files might be overwritten.")

    print(f"\\nStarting project generation for '{project_name}'...")
    
    if sys.version_info < (3, 6):
        print("❌ Error: This script requires Python 3.6 or higher.")
        return

    for file_path, content in project_structure.items():
        full_path = os.path.join(project_root, file_path)
        dir_name = os.path.dirname(full_path)
        
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        try:
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content.strip())
            print(f"✅ Created file: {file_path}")
        except IOError as e:
            print(f"❌ Error creating file {file_path}: {e}")
            return

    print("\\n🎉 Project generation complete!")
    print("\\nNext steps:")
    print(f"1. In your terminal, enter the project directory: cd {project_name}")
    print("2. Run 'npm install' to download all dependencies.")
    print("3. Run 'npm run dev' to start the application.")
    print(f"\\nEnjoy the definitive '{project_name}'!")

if __name__ == "__main__":
    current_directory = os.getcwd()
    create_project(current_directory, PROJECT_NAME)