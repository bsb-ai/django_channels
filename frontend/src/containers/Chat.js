import React from 'react';
import Sidepanel from './Sidepanel/Sidepanel';

class Chat extends React.Component {
    render() {
        return (
            <div id="frame">
                <Sidepanel />
                <div className="content">
                <div className="contact-profile">
                    <img src="data:image/png;base64,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" alt="" />
                    <p>username</p>
                    <div className="social-media">
                    <i className="fa fa-facebook" aria-hidden="true"></i>
                    <i className="fa fa-twitter" aria-hidden="true"></i>
                    <i className="fa fa-instagram" aria-hidden="true"></i>
                    </div>
                </div>
                <div className="messages">
                    <ul id="chat-log">
                    </ul>
                </div>
                <div className="message-input">
                    <div className="wrap">
                    <input id="chat-message-input" type="text" placeholder="Write your message..." />
                    <i className="fa fa-paperclip attachment" aria-hidden="true"></i>
                    <button id="chat-message-submit" className="submit">
                    <i className="fa fa-paper-plane" aria-hidden="true"></i>
                    </button>
                    </div>
                </div>
                </div>
          </div>
        )
    }
}

export default Chat;