START
    INITIALIZE count = 10
    WHILE count is greater than or equal to 1:
        DISPLAY count
        DECREMENT count
        DISPLAY "Enter 'stop' to cancel or press Enter to continue: "
        READ user_input
        IF user_input is "stop"
            DISPLAY "Countdown stopped!"
            BREAK the loop
    END WHILE
END
