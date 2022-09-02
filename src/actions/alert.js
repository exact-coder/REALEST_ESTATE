import { v4 as uuid } from "uuid";
import { REMOVE_ALERT, SET_ALERT } from './types';



export const setAlert= (msg, alertType, timeout =2000) => dispatch => {
    const id = uuid();
    console.log("Actions alert >>>",id);
    dispatch({
        type: SET_ALERT,
        payload: {msg, alertType, id}
    });

    setTimeout(() => dispatch({type: REMOVE_ALERT, payload: id}), timeout);
}