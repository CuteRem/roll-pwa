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