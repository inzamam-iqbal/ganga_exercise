echo -e 'y\n' | ganga;
echo ganga testJob.py '$j.id' | ganga -i gangaJob.py
