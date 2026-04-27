---
title: "Connecting FXCM over FIX (QuickFix engine)"
author: "QuantInsti"
source: "QuantInsti"
url: "https://blog.quantinsti.com/connecting-fxcm-fix-detailed-tutorial/"
date: "2016-10-24"
topics: ["quantitative-trading", "algorithmic-trading"]
---

# Connecting FXCM over FIX (QuickFix engine)

**来源**: [QuantInsti](https://blog.quantinsti.com/connecting-fxcm-fix-detailed-tutorial/)  
**日期**: 2016-10-24  
**作者**: QuantInsti

---

## 原文

Connecting FXCM Over FIX – A Detailed Tutorial

BySunith Reddy

We talked about the defacto standard for message communication in our previous article onFIX protocol.

“The Financial Information Exchange (FIX) Protocol is a message standard developed to facilitate the electronic exchange of information related to securities transactions. It is intended for use between trading partners wishing to automate communications.[1]”

In this article, we are going to take a step further and talk about some operations involved inconnecting FXCM over fix. We will be using the QuickFix engine to code the examples. Quickfix is an open source FIX engine.

“QuickFIXis an open source FIX engine. It integrates with financial applications giving them the connectivity they need to communicate with hundreds of systems around the world that support FIX.QuickFIXgives your applications the power to electronically interact with all these systems using a simple interface.”

You can learn more about QuickFIX fromhere.

Credentials

Just like we had credentials for connecting withInteractive Brokers using IBridgePY, we have credentials here as well. Connecting FCMX over fix will need some credentials which will identify the connecting entity for FXCM. The credentials consist of the following:

Socket connection host, port– where you would be connecting

Sender comp Id– identifies the sender of the message.

Target comp id– identifies the intended recipient of the message

Target sub id– a sub identifier which completes the recipient identification.

In case of quickFix, these credentials need to be configured in a configuration file. The configuration file would look as follows:

# Default settings. These settings are inherited by each# individual session found below

[DEFAULT]

 

BeginString=FIX.4.4

ConnectionType=initiator

HeartBtInt=30

FileStorePath=.\Store

FileLogPath=.\Logs# Start and End times for the FIX session (in UTC)

StartDay=Sunday

StartTime=21:15:00

EndDay=Friday

EndTime=20:00:00

 

UseDataDictionary=Y

DataDictionary=FIXFXCM10.xml

ValidateUserDefinedFields=N

ValidateFieldsHaveValues=N

ValidateFieldsOutOfOrder=N

 

ReconnectInterval=20

ResetOnDisconnect=Y

ResetSeqNumFlag=Y

SendResetSeqNumFlag=Y

ContinueInitializationOnError=Y# Session specific settings along with FIX credentials# supplied by FXCM

[SESSION]

 

SenderCompID=someID

TargetCompID=FXCM

SocketConnectHost=someHost

SocketConnectPort=somePort

TargetSubID=someTargetID

Username=someUsername

Password=somePassword

Logging In

All set? Good, if your configuration is correct then the quickfix engine will initiate the connection. This involves connecting to the host and port, and sending the login request.  The login request is the first message of any session. In case it is not the first message, all messagesthat were sent before the login request are simply ignored.

“All messages sent before login request are ignored.”

The example login message would look as follows:

#Send Username/Password on Logon (35=A)8=FIX.4.49=114 35=A 34=1 49=sendercompId 52=20120927-13:15:34.754 56=FXCM 57=someTargetSubId 553=someUsername 554=somePassword 98=0 108=30 141=Y 10=146

Tags 553 and 554 are meant to pass on the username and password.  Note that 34=1 assumes that this is the first attempt of the day. In other cases it will just be the sequence number of the message. If all credentials are right, then the logon response from FXCM would look as follows

#FXCM Logon response 8=FIX.4.49=92 35=A 34=1 49=FXCM 50=someTargetSubId 52=20120927-13:15:34.810 56=somesenderCompId 98=0 108=30 141=Y 10=187

Note that since the response is being sent by fxcm and the intended recipient is our system, the 49 tag isFXCM (sender)and tag 56 =somesenderCompId(intended recipient).

Once the credentials have been verified and the successful response received, One might want to get a few initialization parameters in place. For eg, what is the state of the market (open/closed), symbol information (lot sizes, ticksizes), etc.  In order to do this, we use theTrading Session Status Request(35=g)

The following code snippet shows how to send the trading session status request

FIX44::TradingSessionStatusRequest request;request.setField(FIX::TradSesReqID(NextId())); request.setField(FIX::SubscriptionRequestType(FIX::SubscriptionRequestType_SNAPSHOT_PLUS_UPDATES)); FIX::Session::sendToTarget(request,session_id);

This sends the request, the response to which is the trading session status message.  The session status message looks like the following

-- Core TradingSessionStatus Message -- 8=FIX.4.49=12384 35=h34=3 49=FXCM 50=U100D1 52=20120828-13:24:52.38756=fx1294946_client158=Market is closed. Any trading functionality is not available.60=20120828-13:24:52325=N 335=2336=FXCM339=2340=2625=U100D19019=09030=Coordinated Universal Time#-- Embedded SecurityList --#NoRelatedSym (This field shows the total number of securities. Below we only show the first 5 to save space)146=69 55=CAD/JPY15=CAD228=1231=1460=4561=19000=189001=39002=0.019003=0.159004=-0.339005=18009076=D9080=19090=09091=09092=09093=09094=500000009095=19096=O55=GBP/CHF15=GBP228=1231=1460=4561=19000=139001=59002=0.00019003=0.159004=-0.379005=13009076=D9080=19090=09091=09092=09093=09094=500000009095=19096=O55=JPN22515=JPY228=100231=1460=7561=19000=10079001=09002=19003=0.079004=-0.099005=1007009076=T9080=29090=259091=19092=259093=19094=10009095=19096=O55=EUR/SEK15=EUR228=1231=1460=4561=19000=329001=59002=0.00019003=-0.829004=0.269005=32009076=D9080=19090=09091=09092=09093=09094=500000009095=19096=O55=AUD/USD15=AUD228=1231=1460=4561=19000=69001=59002=0.00019003=0.639004=-1.319005=6009076=V9080=19090=09091=09092=09093=09094=500000009095=19096=O 

-- FXCM System Parameters --  

NoFXCMParam (This field shows the total number of system parameters)9016=17 

9017=TP_949018=Y9017=BASE_CRNCY9018=USD9017=TRAILING_STOP_USED9018=Y9017=SERVER_TIME_UTC9018=UTC9017=BASE_TIME_ZONE9018=America/New_York9017=EXT_PRICE_TERMINAL9018=PDEMO1_PRICES9017=COND_DIST9018=0.19017=COND_DIST_ENTRY9018=0.19017=TP_1729018=Y9017=BASE_CRNCY_SYMBOL9018=$9017=REPORTS_URL9018=https://fxpa.fxcorporate.com/fxpa/getreport.app/9017=BASE_UNIT_SIZE9018=100009017=END_TRADING_DAY9018=21:00:009017=BASE_CRNCY_PRECISION9018=29017=FixSupport9018=FIXONLY9017=TRAILING_STOP_DYNAMIC9018=Y

9017=FORCE_PASSWORD_CHANGE9018=N10=058

However, we are interested in reading this message from code.  The way to read each of these system parameters is as follows:

int param_count = FIX::IntConvertor::convert(status.getField(9016));

cout << "TSS - FXCM System Parameters" << endl;
 for(int i = 1; i =< param_count; i++)
 {
 FIX::FieldMap map = status.getGroupRef(1,9016);
 string param_name = map.getField(9017);
 string param_value = map.getField(9018);

cout << param_name << " - " << param_value << endl;
 }

FXCM sends additional tags in thetradingSessionStatusmessage. These can be found in thesecurityListandsystemParameters. This information will be used while sending orders.

Custom fields inSecurityList

9001 –symPrecision– precision of the security. Foreg, USD/JPY the value is 3 => the value fields for this symbol are quoted to a precision of 3 decimal places.

9002 –point size– this represents what we mean by a pip for a security. For eg. EUR/USD would show a value of 0.0001 for this field.

9003 –symInterestBuy– the price in the currency of your account for the default lot size of your server. For eg, if your account is in USD and the server default lot size is 10000. Then 9003=0.64 => you will get $0.64 for 10K size.

9004 –symInterestSell– same as above. 9004=-1.48 => you ll pay $1.48 for every 10K size. You can read the default lot size from the tag 9017=BASE_UNIT_SIZE 9018=10000.

9080 –productId– every security belongs to a product type. 1=Forex, 2=Index, 3=Commodity, 4=treasury, 5=bullion. For eg, EUR/USD would be 1.

9090 –conditionalDistanceStop– The minimum distance of the stop orders from the current market price. If you have a buy position, then your stop order must be atleast this distance away from the current bid.

9091 –conditionalDistanceLimit– The minimum distance of the limit order from the current market price. If you have a buy position, then your limit order must be atleast this distance away from the current bid.

9092 –conditionalDistanceEntryStop– The minimum distance for a new stop entry (pending) order. If you want to place a stop entry order to buy then the price of this order must be atleast this distance away from the current ask.

9093 –conditionalDistanceEntryLimit– The minimum distance for a new limit entry (pending) order. If you wanted to place a new limit entry order to buy, then the price of the order must be atleast this distance away from the current ask.

9094 –maxQuantity– maximum size of a single order.

9095 –minQuantity– minimum size of a single order.

9096 –tradingStatus– This indicates whether the destination is open (‘O’) or closed (‘C’).

In addition to the above custom fields, the system parameters are also returned in this message (combination of 9017,9018 tags)

BASE_CRNCY –the currency of your account

SERVER_TIME_UTC –if this field is set to UTC then the server will express all time fields in UTC. If not, then it ll express it in the local timezone

BASE_TIME_ZONE – shows the local timezone of the server for example “Asia/Kolkatta”

COND_DIST– minimum distance between the price of the new stop or limit orders from the current market price. This value is expressed in pips and is generally defaulted to 0.10

COND_DIST_ENTRY– minimum distance between the price of the new stop entry or limit entry orders from the current market price. This value is expressed in pips and is generally defaulted to 0.10

BASE_UNIT_SIZE– minimum order size for FX securities. For CFD securities, we need to check the 9095 tag

END_TRADING_DAY– Timing for the close of the trading day. It is expressed in hh:mm:ss format. This time is always in UTC

Requesting Market Data

After making the connection with the server, we are ready to request for Market Data.MarketDataconsists of a snapshot message and an incremental update message.  TheMarketDataSnapshotFullRefresh(W)message contains the updates to market data. It is obtained as a response to marketdatarequest (v) message.

The following snippet shows how to send themarketdatarequestmessage:

FIX44::MarketDataRequest mdr; mdr.set(FIX::MDReqID(NextId()));mdr.set(FIX::SubscriptionRequestType(FIX::SubscriptionRequestType_SNAPSHOT_PLUS_UPDATES));mdr.set(FIX::MarketDepth(0));mdr.set(FIX::NoMDEntryTypes(2)); FIX44::MarketDataRequest::NoMDEntryTypes types_group;types_group.set(FIX::MDEntryType(FIX::MDEntryType_BID));mdr.addGroup(types_group);types_group.set(FIX::MDEntryType(FIX::MDEntryType_OFFER));mdr.addGroup(types_group); int no_sym = FIX::IntConvertor::convert(security_list.getField(FIX::FIELD::NoRelatedSym));for(int i = 1; i <= no_sym; i++){   FIX44::SecurityList::NoRelatedSym sym_group;   mdr.addGroup(security_list.getGroup(i,sym_group));} FIX::Session::sendToTarget(mdr,session_id);

The samplemarketDataSnapshotFullRefreshmessage looks like this:

8=FIX.4.49=53335=W34=3649=FXCM50=U100D152=2012091313:07:51.38756=fx157369001_client155=AUD/USD228=1231=1262=4460=4 # Number of MDEntries268=4# High 269=7270=1.03902272=20120913273=13:07:49# Low269=8270=1.03843272=20120913273=13:07:49# Bid269=0270=1.04437271=0272=20120913273=13:07:49336=FXCM625=U100D1276=A299=FXCM-AUDUSD-12638558537=1 # Offer269=1270=1.04459271=0272=20120913273=13:07:49336=FXCM625=U100D1276=A299=FXCM-AUDUSD-12638558537=1# Custom FXCM Fields9000=69001=59002=0.00019005=6009011=09020=19080=19090=09091=09092=09093=09094=500000009095=19096=O10=030

MDEntryTypes

The types of data you can receive are referred to as MDEntryTypes in FIX.  FXCM supports:

Bid(0)

Ask(1)

HighPrice(7)

LowPrice(8)

Additional MDEntryTypes such asMDEntryDate,MDEntryTimeetc. are found only once within the first repeating group of the message.

Position Information

Before starting a strategy it is important to always retrieve the position information.  This is done using the Position Report (35=AP) message. One could not only request for a position report but also subscribe to updates. Sending a RequestForPositions (AN) message with subscription Request type (263) set to  1 will subscribe to updates.

PosReqType (tag 724) is used to determine if a received report is an open (indicated by 0) or closed (indicated by 1) position.

When an open position report is received, it also contains the price at which the position was opened (tag 730).   In case of a closed position report,  the price at which the position as closed, as well as some additional tags are present:

9052 – gross P&L of the position.

9040 – rollover interest applied to the position

9053 – commission applied

9043 – close price of the position

Example Position Report

Overview of Basic Order types

Time In Force

Time in force represents the duration for which an order stays in the order book in case it is not executed. The different values possible are:

GTC(Good till cancel) – This means the order stays in force until its executed or cancelled out explicitly. Typically used when you don’t expect the order to be filled immediately. You want to keep the order active until it is filled.

Day- This means the order stays in force till its executed or the day expires.  Typically, this is used when your intent of the order gets obsolete with time.

IOC(Immediate or Cancel) – The order gets filled as much as possible at the time it enters the order book. The remaining gets cancelled. You want to take the fill at a particular price.

FOK(Fill or Kill) – The order either gets completely filled at the time it enters the orderbook or gets cancelled immediately. You are interested in taking the full fill at a particular price.

Order Types

This order will hit the opposite side irrespective of the price. It will take the fill at the next available price as long as the order book is not empty. Typically used when filling the order is more important than the price of the fill. For a market order, the TIF can be GTC, DAY, IOC, FOK.

FIX44::NewOrderSingle order;order.setField(FIX::ClOrdID(NextClOrdID())); order.setField(FIX::Account(account));order.setField(FIX::Symbol("EUR/USD")); order.setField(FIX::Side(FIX::Side_BUY)); order.setField(FIX::TransactTime(FIX::TransactTime())); order.setField(FIX::OrderQty(10000));order.setField(FIX::OrdType(FIX::OrdType_MARKET)); FIX::Session::sendToTarget(order,session_id);

This order is a market order that has a range for the fill price. This provides a protection against slippage of the fill price. The tag 40=4 means it’s a stopLimit order and the stopPrice is set in tag 99. This represents the worst price you are willing to take the fill at. The TIF can be IOC or FOK

FIX44::NewOrderSingle order;order.setField(FIX::ClOrdID(NextClOrdID())); order.setField(FIX::Account(account));order.setField(FIX::Symbol("EUR/USD")); order.setField(FIX::Side(FIX::Side_BUY)); order.setField(FIX::TransactTime(FIX::TransactTime())); order.setField(FIX::OrderQty(10000));order.setField(FIX::OrdType(FIX::OrdType_STOPLIMIT));order.setField(FIX::StopPx(stop)); FIX::Session::sendToTarget(order,session_id);

The order will be filled at a price that is equal or better than the price mentioned in the order message (tag 44).  This order type is used when the price of fill is more important than the fill itself. Supported TIFs are GTC, Day,IOC, FOK.

FIX44::NewOrderSingle order;order.setField(FIX::ClOrdID(NextClOrdID())); order.setField(FIX::Account(account));order.setField(FIX::Symbol("EUR/USD")); order.setField(FIX::Side(FIX::Side_BUY)); order.setField(FIX::TransactTime(FIX::TransactTime())); order.setField(FIX::OrderQty(10000));order.setField(FIX::OrdType(FIX::OrdType_LIMIT)); order.setField(FIX::Price(price)); FIX::Session::sendToTarget(order,session_id);

This is a market order that gets placed when the current market price is worse than your stop price as mentioned in the stopOrder message.  The price of the fill is not guaranteed, as this is a market order. Supported TIFs are GTC and Day.

FIX44::NewOrderSingle order;order.setField(FIX::ClOrdID(NextClOrdID())); order.setField(FIX::Account(account));order.setField(FIX::Symbol("EUR/USD")); order.setField(FIX::Side(FIX::Side_BUY)); order.setField(FIX::TransactTime(FIX::TransactTime())); order.setField(FIX::OrderQty(10000));order.setField(FIX::OrdType(FIX::OrdType_STOP)); order.setField(FIX::StopPx(price)); FIX::Session::sendToTarget(order,session_id);

Example

This piece of code assumes that the quickfix library is installed. The include path needs to be edited accordingly.  This should give a basic understanding of how a FXCM session can be established, market data subscribed, and orders sent.

Main.cpp#include "fix_application.h"

 

// -- FIX Example --

//

// Upon starting this application, a FIX session will be created and the connection sequence will commence. This includes sending a Logon message, a request for TradingSessionStatus. After the responses to these requests are received, you can use the command prompt to test out the functionality seen below in the switch block.

 

int main()

{

            FixApplication app;

            // Start session and Logon

            app.StartSession();

 

            while(true){

                        int command = 0;

                        bool exit = false;

                        cin >> command;

 

                        switch(command){

                        case 0: // Exit example application

                                    exit = true;

                                    break;

                        case 1: // Get positions 

                                    app.GetPositions();

                                    break;

                        case 2: // Subscribe to market data

                                    app.SubscribeMarketData();

                                    break;

                        case 3: // Unsubscribe to market data

                                    app.UnsubscribeMarketData();

                                    break;

                        case 4: // Send market order

                                    app.MarketOrder();

                                    break;

                        }

                        if(exit)

                                    break;

            }

 

            // End session and logout

            app.EndSession();

            while(true){

            } // Wait

            return 0;

}










fix_application.h#ifndef FIXAPPLICATION_H#define FIXAPPLICATION_H#include <iostream>#include <vector>#include "quickfix\Application.h"#include "quickfix\FileLog.h"#include "quickfix\FileStore.h"#include "quickfix\fix44\CollateralInquiry.h"#include "quickfix\fix44\CollateralInquiryAck.h"#include "quickfix\fix44\CollateralReport.h"#include "quickfix\fix44\ExecutionReport.h"#include "quickfix\fix44\MarketDataRequest.h"#include "quickfix\fix44\MarketDataRequestReject.h"#include "quickfix\fix44\MarketDataSnapshotFullRefresh.h"#include "quickfix\fix44\NewOrderList.h"#include "quickfix\fix44\NewOrderSingle.h"#include "quickfix\fix44\PositionReport.h"#include "quickfix\fix44\RequestForPositions.h"#include "quickfix\fix44\RequestForPositionsAck.h"#include "quickfix\fix44\SecurityList.h"#include "quickfix\fix44\TradingSessionStatus.h"#include "quickfix\fix44\TradingSessionStatusRequest.h"#include "quickfix\MessageCracker.h"#include "quickfix\Session.h"#include "quickfix\SessionID.h"#include "quickfix\SessionSettings.h"#include "quickfix\SocketInitiator.h"

 

using namespace std;

using namespace FIX;

 

class FixApplication : public MessageCracker, public Application

{

private:

            SessionSettings  *settings;

            FileStoreFactory *store_factory;

            FileLogFactory   *log_factory;

            SocketInitiator  *initiator;

 

            // Used as a counter for producing unique request identifiers

            unsigned int requestID;

            SessionID sessionID;

            vector<string> list_accountID;

 

            // Custom FXCM FIX fields

            enum FXCM_FIX_FIELDS

            {

                        FXCM_FIELD_PRODUCT_ID      = 9080,

                        FXCM_POS_ID                = 9041,

                        FXCM_POS_OPEN_TIME         = 9042,

                        FXCM_ERROR_DETAILS         = 9029,

                        FXCM_REQUEST_REJECT_REASON = 9025,

                        FXCM_USED_MARGIN           = 9038,

                        FXCM_POS_CLOSE_TIME        = 9044,

                        FXCM_MARGIN_CALL           = 9045,

                        FXCM_ORD_TYPE              = 9050,

                        FXCM_ORD_STATUS            = 9051,

                        FXCM_CLOSE_PNL             = 9052,

                        FXCM_SYM_POINT_SIZE        = 9002,

                        FXCM_SYM_PRECISION         = 9001,

                        FXCM_TRADING_STATUS        = 9096,

                        FXCM_PEG_FLUCTUATE_PTS     = 9061,

                        FXCM_NO_PARAMS             = 9016,

                        FXCM_PARAM_NAME            = 9017,

                        FXCM_PARAM_VALUE           = 9018

            };

 

public:

            FixApplication();

            // FIX Namespace. These are callbacks which indicate when the session is created,

            // when we logon and logout, and when messages are exchanged 

            void onCreate(const SessionID& session_ID);

            void onLogon(const SessionID& session_ID);

            void onLogout(const SessionID& session_ID);

            void toAdmin(Message& message, const SessionID& session_ID);

            void toApp(Message& message, const SessionID& session_ID);

            void fromAdmin(const Message& message, const SessionID& session_ID);

            void fromApp(const Message& message, const SessionID& session_ID);

 

            // Overloaded onMessage methods used in conjuction with MessageCracker class. FIX::MessageCracker

            // receives a generic Message in the FIX fromApp and fromAdmin callbacks, constructs the

            // message sub type and invokes the appropriate onMessage method below.

            void onMessage(const FIX44::TradingSessionStatus& tss, const SessionID& session_ID);

            void onMessage(const FIX44::CollateralInquiryAck& ack, const SessionID& session_ID);

            void onMessage(const FIX44::CollateralReport& cr, const SessionID& session_ID);

            void onMessage(const FIX44::RequestForPositionsAck& ack, const SessionID& session_ID);

            void onMessage(const FIX44::PositionReport& pr, const SessionID& session_ID);

            void onMessage(const FIX44::MarketDataRequestReject& mdr, const SessionID& session_ID);

            void onMessage(const FIX44::MarketDataSnapshotFullRefresh& mds, const SessionID& session_ID);

            void onMessage(const FIX44::ExecutionReport& er, const SessionID& session_ID);

 

            // Starts the FIX session. Throws FIX::ConfigError exception if our configuration settings

            // do not pass validation required to construct SessionSettings 

            void StartSession();

            // Logout and end session 

            void EndSession();

 

            // Sends TradingSessionStatusRequest message in order to receive as a response the

            // TradingSessionStatus message

            void GetTradingStatus();

            // Sends the CollateralInquiry message in order to receive as a response the

            // CollateralReport message.

            void GetAccounts();

            // Sends RequestForPositions which will return PositionReport messages if positions

            // matching the requested criteria exist; otherwise, a RequestForPositionsAck will be

            // sent with the acknowledgement that no positions exist. In our example, we request

            // positions for all accounts under our login

            void GetPositions();

            // Subscribes to the EUR/USD trading security

            void SubscribeMarketData();

            // Unsubscribes from the EUR/USD trading security 

            void UnsubscribeMarketData();

            // Sends a basic NewOrderSingle message to buy EUR/USD at the 

            // current market price

            void MarketOrder();

            // Generate string value used to populate the fields in each message

            // which are used as a custom identifier

            string NextRequestID();

            // Adds string accountIDs to our vector<string> being used to

            // account for the accountIDs under our login

            void RecordAccount(string accountID);

};#endif // FIXAPPLICATION_H


fix_application.cpp#include "fix_application.h"



FixApplication::FixApplication()

{

            // Initialize unsigned int requestID to 1. We will use this as a 

            // counter for making request IDs

            requestID = 1;

}

 

// Gets called when quickfix creates a new session. A session comes into and remains in existence

// for the life of the application.

void FixApplication::onCreate(const SessionID& session_ID)

{

            // FIX Session created. We must now logon. QuickFIX will automatically send

            // the Logon(A) message

            cout << "Session -> created" << endl;

            sessionID = session_ID;

}

 

// Notifies you when a valid logon has been established with FXCM.

void FixApplication::onLogon(const SessionID& session_ID)

{

            // Session logon successful. Now we request TradingSessionStatus which is

            // used to determine market status (open or closed), to get a list of securities,

            // and to obtain important FXCM system parameters 

            cout << "Session -> logon" << endl;

            GetTradingStatus();

}

 

// Notifies you when an FIX session is no longer online. This could happen during a normal logout

// exchange or because of a forced termination or a loss of network connection. 

void FixApplication::onLogout(const SessionID& session_ID)

{

            // Session logout 

            cout << "Session -> logout" << endl;

}

 

// Provides you with a peak at the administrative messages that are being sent from your FIX engine 

// to FXCM.

void FixApplication::toAdmin(Message& message, const SessionID& session_ID)

{

            // If the Admin message being sent to FXCM is of typle Logon (A), we want

            // to set the Username and Password fields. We want to catch this message as it

            // is going out.

            string msg_type = message.getHeader().getField(FIELD::MsgType);

            if(msg_type == "A"){

                        // Get both username and password from our settings file. Then set these

                        // respective fields

                        string user = settings->get().getString("Username");

                        string pass = settings->get().getString("Password");

                        message.setField(Username(user));

                        message.setField(Password(pass));

            }

            // All messages sent to FXCM must contain the TargetSubID field (both Administrative and

            // Application messages). Here we set this.

            string sub_ID = settings->get().getString("TargetSubID");

            message.getHeader().setField(TargetSubID(sub_ID));

}

 

// A callback for application messages that you are being sent to a counterparty. 

void FixApplication::toApp(Message& message, const SessionID& session_ID)

{

            // All messages sent to FXCM must contain the TargetSubID field (both Administrative and

            // Application messages). Here we set this.

            string sub_ID = settings->get().getString("TargetSubID");

            message.getHeader().setField(TargetSubID(sub_ID));

}

 

// Notifies you when an administrative message is sent from FXCM to your FIX engine. 

void FixApplication::fromAdmin(const Message& message, const SessionID& session_ID)

{

            // Call MessageCracker.crack method to handle the message by one of our 

            // overloaded onMessage methods below

            crack(message, session_ID);

}

 

// One of the core entry points for your FIX application. Every application level request will come through here. 

void FixApplication::fromApp(const Message& message, const SessionID& session_ID)

{

            // Call MessageCracker.crack method to handle the message by one of our 

            // overloaded onMessage methods below

            crack(message, session_ID);

}

 

// The TradingSessionStatus message is used to provide an update on the status of the market. Furthermore, 

// this message contains useful system parameters as well as information about each trading security (embedded SecurityList).

// TradingSessionStatus should be requested upon successful Logon and subscribed to. The contents of the

// TradingSessionStatus message, specifically the SecurityList and system parameters, should dictate how fields

// are set when sending messages to FXCM.

void FixApplication::onMessage(const FIX44::TradingSessionStatus& tss, const SessionID& session_ID)

{

            // Check TradSesStatus field to see if the trading desk is open or closed

            // 2 = Open; 3 = Closed

            string trad_status = tss.getField(FIELD::TradSesStatus);

            cout << "TradingSessionStatus -> TradSesStatus -" << trad_status << endl;

            // Within the TradingSessionStatus message is an embeded SecurityList. From SecurityList we can see

            // the list of available trading securities and information relevant to each; e.g., point sizes,

            // minimum and maximum order quantities by security, etc. 

            cout << "  SecurityList via TradingSessionStatus -> " << endl;

            int symbols_count = IntConvertor::convert(tss.getField(FIELD::NoRelatedSym));

            for(int i = 1; i <= symbols_count; i++){

                        // Get the NoRelatedSym group and for each, print out the Symbol value

                        FIX44::SecurityList::NoRelatedSym symbols_group;

                        tss.getGroup(i,symbols_group);

                        string symbol = symbols_group.getField(FIELD::Symbol);

                        cout << "    Symbol -> " << symbol << endl;

            }

            // Also within TradingSessionStatus are FXCM system parameters. This includes important information

            // such as account base currency, server time zone, the time at which the trading day ends, and more.

            cout << "  System Parameters via TradingSessionStatus -> " << endl;

            // Read field FXCMNoParam (9016) which shows us how many system parameters are 

            // in the message

            int params_count = IntConvertor::convert(tss.getField(FXCM_NO_PARAMS)); // FXCMNoParam (9016)

            for(int i = 1; i < params_count; i++){

                        // For each paramater, print out both the name of the paramater and the value of the 

                        // paramater. FXCMParamName (9017) is the name of the paramater and FXCMParamValue(9018)

                        // is of course the paramater value

                        FIX::FieldMap field_map = tss.getGroupRef(i,FXCM_NO_PARAMS);

                        cout << "    Param Name -> " << field_map.getField(FXCM_PARAM_NAME) 

                                    << " - Param Value -> " << field_map.getField(FXCM_PARAM_VALUE) << endl;

            }

            // Request accounts under our login

            GetAccounts();

 

            // ** Note on Text(58) ** 

            // You will notice that Text(58) field is always set to "Market is closed. Any trading

            // functionality is not available." This field is always set to this value; therefore, do not 

            // use this field value to determine if the trading desk is open. As stated above, use TradSesStatus for this purpose

}

 

void FixApplication::onMessage(const FIX44::CollateralInquiryAck& ack, const SessionID& session_ID)

{

 

}

 

// CollateralReport is a message containing important information for each account under the login. It is returned

// as a response to CollateralInquiry. You will receive a CollateralReport for each account under your login.

// Notable fields include Account(1) which is the AccountID and CashOutstanding(901) which is the account balance

void FixApplication::onMessage(const FIX44::CollateralReport& cr, const SessionID& session_ID)

{

            cout << "CollateralReport -> " << endl;

            string accountID = cr.getField(FIELD::Account);

            // Get account balance, which is the cash balance in the account, not including any profit

            // or losses on open trades

            string balance = cr.getField(FIELD::CashOutstanding);

            cout << "  AccountID -> " << accountID << endl;

            cout << "  Balance -> " << balance << endl;

            // The CollateralReport NoPartyIDs group can be inspected for additional account information

            // such as AccountName or HedgingStatus

            FIX44::CollateralReport::NoPartyIDs group;

            cr.getGroup(1,group); // CollateralReport will only have 1 NoPartyIDs group

            cout << "  Parties -> "<< endl;

            // Get the number of NoPartySubIDs repeating groups

            int number_subID = IntConvertor::convert(group.getField(FIELD::NoPartySubIDs));

            // For each group, print out both the PartySubIDType and the PartySubID (the value)

            for(int u = 1; u <= number_subID; u++){

                        FIX44::CollateralReport::NoPartyIDs::NoPartySubIDs sub_group;

                        group.getGroup(u,sub_group);

 

                        string sub_type = sub_group.getField(FIELD::PartySubIDType);

                        string sub_value = sub_group.getField(FIELD::PartySubID);

                        cout << "    " << sub_type << " -> " << sub_value << endl;

            }

            // Add the accountID to our vector<string> being used to track all

            // accounts under our login

            RecordAccount(accountID);

}

 

void FixApplication::onMessage(const FIX44::RequestForPositionsAck& ack, const SessionID& session_ID)

{

            string pos_reqID = ack.getField(FIELD::PosReqID);

            cout << "RequestForPositionsAck -> PosReqID - " << pos_reqID << endl;

 

            // If a PositionReport is requested and no positions exist for that request, the Text field will

            // indicate that no positions mathced the requested criteria 

            if(ack.isSetField(FIELD::Text))

                        cout << "RequestForPositionsAck -> Text - " << ack.getField(FIELD::Text) << endl;

}

 

void FixApplication::onMessage(const FIX44::PositionReport& pr, const SessionID& session_ID)

{

            // Print out important position related information such as accountID and symbol 

            string accountID = pr.getField(FIELD::Account);

            string symbol = pr.getField(FIELD::Symbol);

            string positionID = pr.getField(FXCM_POS_ID);

            string pos_open_time = pr.getField(FXCM_POS_OPEN_TIME);

            cout << "PositionReport -> " << endl;

            cout << "   Account -> " << accountID << endl;

            cout << "   Symbol -> " << symbol << endl;

            cout << "   PositionID -> " << positionID << endl;

            cout << "   Open Time -> " << pos_open_time << endl;

}

 

void FixApplication::onMessage(const FIX44::MarketDataRequestReject& mdr, const SessionID& session_ID)

{

            // If MarketDataRequestReject is returned as the result of a MarketDataRequest message,

            // print out the contents of the Text field but first check that it is set

            cout << "MarketDataRequestReject -> " << endl;

            if(mdr.isSetField(FIELD::Text)){

                        cout << " Text -> " << mdr.getField(FIELD::Text) << endl;

            }

}

 

void FixApplication::onMessage(const FIX44::MarketDataSnapshotFullRefresh& mds, const SessionID& session_ID)

{

            // Get symbol name of the snapshot; e.g., EUR/USD. Our example only subscribes to EUR/USD so 

            // this is the only possible value

            string symbol = mds.getField(FIELD::Symbol);

            // Declare variables for both the bid and ask prices. We will read the MarketDataSnapshotFullRefresh

            // message for tthese values

            double bid_price = 0;

            double ask_price = 0;

            // For each MDEntry in the message, inspect the NoMDEntries group for

            // the presence of either the Bid or Ask (Offer) type 

            int entry_count = IntConvertor::convert(mds.getField(FIELD::NoMDEntries));

            for(int i = 1; i < entry_count; i++){

                        FIX44::MarketDataSnapshotFullRefresh::NoMDEntries group;

                        mds.getGroup(i,group);

                        string entry_type = group.getField(FIELD::MDEntryType);

                        if(entry_type == "0"){ // Bid

                                    bid_price = DoubleConvertor::convert(group.getField(FIELD::MDEntryPx));

                        }else if(entry_type == "1"){ // Ask (Offer)

                                    ask_price = DoubleConvertor::convert(group.getField(FIELD::MDEntryPx));

                        }

            }

            cout << "MarketDataSnapshotFullRefresh -> Symbol - " << symbol 

                        << " Bid - " << bid_price << " Ask - " << ask_price << endl; 

}

 

void FixApplication::onMessage(const FIX44::ExecutionReport& er, const SessionID& session_ID)

{

            cout << "ExecutionReport -> " << endl;

            cout << "  ClOrdID -> " << er.getField(FIELD::ClOrdID) << endl; 

            cout << "  Account -> " << er.getField(FIELD::Account) << endl;

            cout << "  OrderID -> " << er.getField(FIELD::OrderID) << endl;

            cout << "  LastQty -> " << er.getField(FIELD::LastQty) << endl;

            cout << "  CumQty -> " << er.getField(FIELD::CumQty) << endl;

            cout << "  ExecType -> " << er.getField(FIELD::ExecType) << endl;

            cout << "  OrdStatus -> " << er.getField(FIELD::OrdStatus) << endl;

 

            // ** Note on order status. ** 

            // In order to determine the status of an order, and also how much an order is filled, we must

            // use the OrdStatus and CumQty fields. There are 3 possible final values for OrdStatus: Filled (2),

            // Rejected (8), and Cancelled (4). When the OrdStatus field is set to one of these values, you know

            // the execution is completed. At this time the CumQty (14) can be inspected to determine if and how

            // much of an order was filled.

}

 

// Starts the FIX session. Throws FIX::ConfigError exception if our configuration settings

// do not pass validation required to construct SessionSettings 

void FixApplication::StartSession()

{

            try{

                        settings      = new SessionSettings("settings.cfg");

                        store_factory = new FileStoreFactory(* settings);

                        log_factory   = new FileLogFactory(* settings);

                        initiator     = new SocketInitiator(* this, * store_factory, * settings, * log_factory/*Optional*/);

                        initiator->start();

            }catch(ConfigError error){

                        cout << error.what() << endl;

            }

}

 

// Logout and end session 

void FixApplication::EndSession()

{

            initiator->stop();

            delete initiator;

            delete settings;

            delete store_factory;

            delete log_factory;

}

 

// Sends TradingSessionStatusRequest message in order to receive as a response the

// TradingSessionStatus message

void FixApplication::GetTradingStatus()

{

            // Request TradingSessionStatus message 

            FIX44::TradingSessionStatusRequest request;

            request.setField(TradSesReqID(NextRequestID()));

            request.setField(TradingSessionID("FXCM"));

            request.setField(SubscriptionRequestType(SubscriptionRequestType_SNAPSHOT));

            Session::sendToTarget(request, sessionID);

}

 

// Sends the CollateralInquiry message in order to receive as a response the

// CollateralReport message.

void FixApplication::GetAccounts()

{

            // Request CollateralReport message. We will receive a CollateralReport for each

            // account under our login

            FIX44::CollateralInquiry request;

            request.setField(CollInquiryID(NextRequestID()));

            request.setField(TradingSessionID("FXCM"));

            request.setField(SubscriptionRequestType(SubscriptionRequestType_SNAPSHOT));

            Session::sendToTarget(request, sessionID);

}

 

// Sends RequestForPositions which will return PositionReport messages if positions

// matching the requested criteria exist; otherwise, a RequestForPositionsAck will be

// sent with the acknowledgement that no positions exist. In our example, we request

// positions for all accounts under our login

void FixApplication::GetPositions()

{

            // Here we will get positions for each account under our login. To do this,

            // we will send a RequestForPositions message that contains the accountID 

            // associated with our request. For each account in our list, we send

            // RequestForPositions. 

            int total_accounts = (int)list_accountID.size();

            for(int i = 0; i < total_accounts; i++){

                        string accountID = list_accountID.at(i);

                        // Set default fields

                        FIX44::RequestForPositions request;

                        request.setField(PosReqID(NextRequestID()));

                        request.setField(PosReqType(PosReqType_POSITIONS));

                        // AccountID for the request. This must be set for routing purposes. We must

                        // also set the Parties AccountID field in the NoPartySubIDs group

                        request.setField(Account(accountID)); 

                        request.setField(SubscriptionRequestType(SubscriptionRequestType_SNAPSHOT));

                        request.setField(AccountType(

                                    AccountType_ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS_AND_IS_CROSS_MARGINED));

                        request.setField(TransactTime());

                        request.setField(ClearingBusinessDate());

                        request.setField(TradingSessionID("FXCM"));

                        // Set NoPartyIDs group. These values are always as seen below

                        request.setField(NoPartyIDs(1));

                        FIX44::RequestForPositions::NoPartyIDs parties_group;

                        parties_group.setField(PartyID("FXCM ID"));

                        parties_group.setField(PartyIDSource('D'));

                        parties_group.setField(PartyRole(3));

                        parties_group.setField(NoPartySubIDs(1));

                        // Set NoPartySubIDs group

                        FIX44::RequestForPositions::NoPartyIDs::NoPartySubIDs sub_parties;

                        sub_parties.setField(PartySubIDType(PartySubIDType_SECURITIES_ACCOUNT_NUMBER));

                        // Set Parties AccountID

                        sub_parties.setField(PartySubID(accountID));

                        // Add NoPartySubIds group

                        parties_group.addGroup(sub_parties);

                        // Add NoPartyIDs group

                        request.addGroup(parties_group);

                        // Send request

                        Session::sendToTarget(request, sessionID);

            }

}

 

// Subscribes to the EUR/USD trading security

void FixApplication::SubscribeMarketData()

{

            // Subscribe to market data for EUR/USD

            string request_ID = "EUR_USD_Request_";

            FIX44::MarketDataRequest request;

            request.setField(MDReqID(request_ID));

            request.setField(SubscriptionRequestType(

                        SubscriptionRequestType_SNAPSHOT_PLUS_UPDATES));

            request.setField(MarketDepth(0));

            request.setField(NoRelatedSym(1));

 

            // Add the NoRelatedSym group to the request with Symbol

            // field set to EUR/USD

            FIX44::MarketDataRequest::NoRelatedSym symbols_group;

            symbols_group.setField(Symbol("EUR/USD"));

            request.addGroup(symbols_group);

 

            // Add the NoMDEntryTypes group to the request for each MDEntryType

            // that we are subscribing to. This includes Bid, Offer, High, and Low

            FIX44::MarketDataRequest::NoMDEntryTypes entry_types;

            entry_types.setField(MDEntryType(MDEntryType_BID));

            request.addGroup(entry_types);

            entry_types.setField(MDEntryType(MDEntryType_OFFER));

            request.addGroup(entry_types);

            entry_types.setField(MDEntryType(MDEntryType_TRADING_SESSION_HIGH_PRICE));

            request.addGroup(entry_types);

            entry_types.setField(MDEntryType(MDEntryType_TRADING_SESSION_LOW_PRICE));

            request.addGroup(entry_types);

 

            Session::sendToTarget(request, sessionID);

}

 

// Unsubscribes from the EUR/USD trading security 

void FixApplication::UnsubscribeMarketData()

{

            // Unsubscribe from EUR/USD. Note that our request_ID is the exact same

            // that was sent for our request to subscribe. This is necessary to 

            // unsubscribe. This request below is identical to our request to subscribe

            // with the exception that SubscriptionRequestType is set to

            // "SubscriptionRequestType_DISABLE_PREVIOUS_SNAPSHOT_PLUS_UPDATE_REQUEST"

            string request_ID = "EUR_USD_Request_";

            FIX44::MarketDataRequest request;

            request.setField(MDReqID(request_ID));

            request.setField(SubscriptionRequestType(

                        SubscriptionRequestType_DISABLE_PREVIOUS_SNAPSHOT_PLUS_UPDATE_REQUEST));

            request.setField(MarketDepth(0));

            request.setField(NoRelatedSym(1));

 

            // Add the NoRelatedSym group to the request with Symbol

            // field set to EUR/USD

            FIX44::MarketDataRequest::NoRelatedSym symbols_group;

            symbols_group.setField(Symbol("EUR/USD"));

            request.addGroup(symbols_group);

 

            // Add the NoMDEntryTypes group to the request for each MDEntryType

            // that we are subscribing to. This includes Bid, Offer, High, and Low

            FIX44::MarketDataRequest::NoMDEntryTypes entry_types;

            entry_types.setField(MDEntryType(MDEntryType_BID));

            request.addGroup(entry_types);

            entry_types.setField(MDEntryType(MDEntryType_OFFER));

            request.addGroup(entry_types);

            entry_types.setField(MDEntryType(MDEntryType_TRADING_SESSION_HIGH_PRICE));

            request.addGroup(entry_types);

            entry_types.setField(MDEntryType(MDEntryType_TRADING_SESSION_LOW_PRICE));

            request.addGroup(entry_types);

 

            Session::sendToTarget(request, sessionID);

}

 

// Sends a basic NewOrderSingle message to buy EUR/USD at the 

// current market price

void FixApplication::MarketOrder()

{

            // For each account in our list, send a NewOrderSingle message

            // to buy EUR/USD. What differentiates this message is the

            // accountID

            int total_accounts = (int)list_accountID.size();

            for(int i = 0; i < total_accounts; i++){

                        string accountID = list_accountID.at(i);

                        FIX44::NewOrderSingle request;

                        request.setField(ClOrdID(NextRequestID()));            

                        request.setField(Account(accountID));

                        request.setField(Symbol("EUR/USD"));

                        request.setField(TradingSessionID("FXCM"));

                        request.setField(TransactTime());

                        request.setField(OrderQty(10000));

                        request.setField(Side(FIX::Side_BUY));

                        request.setField(OrdType(OrdType_MARKET));

                        request.setField(TimeInForce(TimeInForce_GOODTILLCANCEL));

                        Session::sendToTarget(request, sessionID);

            }

}

 

// Generate string value used to populate the fields in each message

// which are used as a custom identifier

string FixApplication::NextRequestID()

{

            if(requestID == 65535)

                        requestID = 1;

 

            requestID++;

            string next_ID = IntConvertor::convert(requestID);

            return next_ID;

}

 

// Adds string accountIDs to our vector<string> being used to

// account for the accountIDs under our login

void FixApplication::RecordAccount(string accountID)

{

            int size = (int)list_accountID.size();

            if(size == 0){

                        list_accountID.push_back(accountID);

            }else{

                        for(int i = 0; i < size; i++){

                                    if(list_accountID.at(i) == accountID)

                                                break;

                                    if(i == size - 1){

                                                list_accountID.push_back(accountID);

                                    }

                        }

            }

}

Next Step

FXCM is definitely one of the leading online trading platforms that allow retail clients to speculate on forex. If you’re a retail trader or a tech professional looking to start your own automated trading desk or curious to know more about forex and algorithmic trading, begin with basic concepts likeautomated trading architecture,market microstructure,strategy backtesting systemandorder management system. Startlearning algo tradingtoday!

Disclaimer: All investments and trading in the stock market involve risk. Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. The trading strategies or related information mentioned in this article is for informational purposes only.

Download The Code

FXCM over FIX Tutorial - C++ Code

Login to Download

---

*Imported from QuantInsti Blog on 2026-04-27*
