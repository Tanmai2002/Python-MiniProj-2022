r(datetime.date.today()),"Time of Sleep" :t,'Quality':np.mean(temp.flatten()>0)*3/2*100}
    # toLog2 = {"date":str(datetime.date.today()),"timeOfSleep" :t,'quality':np.mean(temp.flatten()>0)*3/2*100}
    # pushLog(toLog2)

    # df=df.append(toLog,ignore_index=True)

    # df.to_csv('Daily_logs.csv',index=False)
    # logs.to_csv('logs.csv')