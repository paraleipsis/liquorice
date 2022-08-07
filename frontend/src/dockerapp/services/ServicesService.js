import axios from 'axios';
const API_URL = 'http://localhost:7001';

export default class ServicesService{
	
	constructor(){}
	
	
	async getServices() {
		const url = `${API_URL}/dockerapp/services/`;
        const response = await axios.get(url);
        const data = await response.data;
		return data;
	}  
	
}