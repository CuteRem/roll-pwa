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