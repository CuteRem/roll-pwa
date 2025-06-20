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