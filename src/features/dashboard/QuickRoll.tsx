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
    const [customOptions, setCustomOptions] = useState('选项A\n选项B\n选项C');
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
            const options = customOptions.split(/[\n,，]/).map(s => s.trim()).filter(Boolean);
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