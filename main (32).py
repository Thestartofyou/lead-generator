import csv

def generate_leads():
    leads = []
    while True:
        name = input("Enter name (or 'exit' to quit): ")
        if name == 'exit':
            break
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        zip_code = input("Enter zip code: ")
        lead = {'name': name, 'email': email, 'phone': phone, 'city': city, 'state': state, 'zip_code': zip_code}
        leads.append(lead)
    return leads

def save_leads(leads):
    with open('leads.csv', mode='a') as csv_file:
        fieldnames = ['name', 'email', 'phone', 'city', 'state', 'zip_code']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # If the file is empty, add a header row
        csv_file.seek(0)
        first_char = csv_file.read(1)
        if not first_char:
            writer.writeheader()

        # Write the leads to the file
        for lead in leads:
            writer.writerow(lead)

if __name__ == '__main__':
    leads = generate_leads()
    save_leads(leads)
